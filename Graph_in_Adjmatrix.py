#This algorithm print 
#undirected Graph like Matrix
#
#Author: Trung Vo | vtvo90@outlook.com

from collections import defaultdict
class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        #Another way
        #self.adjMatrix = [[] for i in range(size)]
        self.size = size

    # Add edges
    def addEdges(self, source, des):
        self.adjMatrix[source][des] = 1
        self.adjMatrix[des][source] = 1

    # Remove edges
    def remove_edge(self, source, des):
        self.adjMatrix[source][des] = 0
        self.adjMatrix[des][source] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print('[', end =""),
            for val in row:
                print('{:0}'.format(val), end =" ")
            print(']'),
    
    #Convert Matrix as List
    def convert(self):
        adjList = defaultdict(list)
        for i in range(self.size):
            for j in range(len(self.adjMatrix[i])):
                if self.adjMatrix[i][j] ==1:
                    adjList[i].append(j)
        return adjList

        
if __name__ == '__main__':
    g = Graph(5)
    g.addEdges(0, 1)
    g.addEdges(0, 2)
    g.addEdges(1, 2)
    g.addEdges(2, 4)
    g.addEdges(2, 3)
    g.addEdges(3, 4)
    g.addEdges(4, 1)

    g.print_matrix()

    adList = g.convert()
    print("Print matrix as List: ")
    for i in adList:
        print(i, end="")
        for j in adList[i]:
            print(" -> {}".format(j), end="")
        print()