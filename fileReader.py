
def readData(filename):
    f = open(filename, 'r')
    x = []
    for line in f:
        splited = line.split(' ')
        aux = []
        aux.append(float(splited[0]))
        aux.append(float(splited[1]))
        x.append(aux)
    return x


if __name__ == '__main__':
    print(readData('datasets/data.dat'))