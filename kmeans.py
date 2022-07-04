import copy
from math import sqrt
import random
import fileReader
import plot
import argparse

# distance between a and b
def euclideanDistance(ax, ay, bx, by):
    return sqrt((ax - bx) ** 2 + (ay - by) ** 2)


def variance(data, labels, centroids):
    var = []
    for j in range(len(centroids)):
        n = 0
        sum = 0.0
        for i in range(len(labels)):
            if labels[i] == j:
                n += 1
                sum += euclideanDistance(data[i][0], data[i][1], centroids[j][0], centroids[j][1])**2
        if n > 0:
            var.append(sum/n)
        else:
            var.append(0)
    sum = 0
    for v in var:
        sum += v
    return sum/len(var)


# return the label for the nearest centroid
def nearestCentroid(x, centroids):
    label = 0
    minimum = euclideanDistance(x[0], x[1], centroids[0][0], centroids[0][1])
    for i in range(1, len(centroids)):
        if euclideanDistance(x[0], x[1], centroids[i][0], centroids[i][1]) < minimum:
            minimum = euclideanDistance(x[0], x[1], centroids[i][0], centroids[i][1])
            label = i
    return label


#randomize labels for each entry in the dataset
def randomizeLabels(size, k):
    labels = []
    for i in range(size):
         labels.append(random.randint(0, k-1))
    return labels


#labels each data entry following the nearest centroid
def cluster(data, labels, centroides):
    changed = False

    for i in range(len(data)):
        oldLabel = labels[i]
        labels[i] = nearestCentroid(data[i], centroides)
        if labels[i] != oldLabel:
            changed = True
    return labels, changed

#update the position of each centroid to match the center of the cluster
def updateCentroids(data, labels, centroids):
    for j in range(len(centroids)):
        neighbors = 0
        acc0 = 0
        acc1 = 0
        for i in range(len(data)):
            if labels[i] == j:
                neighbors += 1
                acc0 += data[i][0]
                acc1 += data[i][1]
        if(neighbors > 0):
            centroids[j][0] = acc0 / neighbors
            centroids[j][1] = acc1 / neighbors
        else:
            centroids[j][0] = 0
            centroids[j][1] = 0
    return centroids


def kmeans(k, data, maxIterations, snapshot=False):
    centroids = []
    changed = True
    labelSnapshots = []
    centroidsSnapshots = []

    for i in range(k):
        centroide = []
        centroide.append(0.0)
        centroide.append(0.0)
        centroids.append(centroide)
        # print(i)
    labels = randomizeLabels(len(data), k)
    i = 0
    if snapshot:
        labelSnapshots.append(labels.copy())
        # centroidsSnapshots.append(copy.deepcopy(centroids))
    while (changed and i < maxIterations):
        i += 1
        centroids = updateCentroids(data, labels, centroids)
        labels, changed = cluster(data, labels, centroids)
        if snapshot:
            labelSnapshots.append(labels.copy())
            centroidsSnapshots.append(copy.deepcopy(centroids))

    if snapshot:
        return labelSnapshots, centroidsSnapshots

    return labels, centroids

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='kmeans clustering')
    parser.add_argument('-k', type=int, dest='clusters', help='number of clusters', default=3)
    parser.add_argument('-f', type=str, dest='filename', help='input filename', default='datasets/data.dat')
    parser.add_argument('-i', type=int, dest='maxIterations', help='max iterations', default='1000')
    parser.add_argument('-o', type=str, dest='outputFile', help='output filename', default=None)

    args = parser.parse_args()

    data = fileReader.readData(args.filename)

    labels, centroids = kmeans(args.clusters, data, args.maxIterations)
    plot.plotKmeans(data, labels, centroids, args.outputFile)


