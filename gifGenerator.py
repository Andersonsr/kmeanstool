import argparse
import os
import imageio
import fileReader
import kmeans
import plot

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gif maker')
    parser.add_argument('-k', type=int, dest='clusters', help='number of clusters', default=3)
    parser.add_argument('-f', type=str, dest='filename', help='input filename', default='datasets/data.dat')
    parser.add_argument('-i', type=int, dest='maxIterations', help='max iterations', default='1000')
    parser.add_argument('-o', type=str, dest='outputFile', help='output filename', default='output.gif')
    parser.add_argument('-s', type=int, dest='fps', help='frames per second', default=1)
    args = parser.parse_args()

    data = fileReader.readData(args.filename)
    labels, centroids = kmeans.kmeans(args.clusters, data, args.maxIterations, snapshot=True)

    for i in range(len(labels)):
        plot.plotKmeans(data, labels[i], centroids[i-1] if i else None, 'frame'+str(i)+'.png')

    frames = []
    for i in range(len(labels)):
        frames.append(imageio.imread('frame'+str(i)+'.png'))

    imageio.mimsave(args.outputFile, frames, format='GIF', fps=args.fps)
    for i in range(len(labels)):
        os.remove('frame'+str(i)+'.png')
