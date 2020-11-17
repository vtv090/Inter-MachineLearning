


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, numVertex):
        self.V = numVertex
        self.graph = [None]* self.V

    def addEdge(self, src, des):
        node = AdjNode(des)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[des]
        self.graph[des] = node

    def printGraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end ="")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":

    graph = Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 2)

    graph.printGraph()