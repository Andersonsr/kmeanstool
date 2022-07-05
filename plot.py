import matplotlib.pyplot as plt
import matplotlib._color_data as mcd

def plotKmeans(data, labels, centroids, outputfile):
    colors = [name for name in mcd.XKCD_COLORS]

    for i in range(len(data)):
        plt.plot(data[i][0], data[i][1], 'p', color=colors[labels[i]])
    if centroids is not None:
        for i in range(len(centroids)):
            plt.plot(centroids[i][0], centroids[i][1], 'p', color='red')

    plt.title("K-means")
    plt.xlabel("x1")
    plt.ylabel("x2")

    if outputfile is None:
        plt.show()
    else:
        plt.savefig(outputfile)
    plt.close()

def plotElbow(k, variance):
    plt.plot(k, variance)

    plt.title("Elbow")
    plt.xlabel("k")
    plt.ylabel("variance")
    plt.show()

