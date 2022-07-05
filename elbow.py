import argparse

import fileReader
import kmeans
import plot

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='k means elbow method')
    parser.add_argument('-s', type=int, default=2, dest='ini', help='initial k')
    parser.add_argument('-e', type=int, default=10, dest='fin', help='final k')
    parser.add_argument('-f', type=str, default='datasets/data2.dat', dest='filename', help='input filename')
    parser.add_argument('-o', type=str, default=None, dest='output', help='output filename')
    parser.add_argument('-i', type=str, default=1000, dest='maxIterations', help='max iterations')
    args = parser.parse_args()

    data = fileReader.readData(args.filename)
    results = []
    ks = []
    for k in range(args.ini, args.fin+1):
        labels, centroids = kmeans.kmeans(k, data, args.maxIterations)
        var = kmeans.variance(data, labels, centroids)
        ks.append(k)
        results.append(var)

    plot.plotElbow(ks, results)