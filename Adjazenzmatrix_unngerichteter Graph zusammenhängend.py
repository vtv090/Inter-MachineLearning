class Graph:
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.adj = [[] for i in range(numNodes)]
    
    def addEdge(self, src, des):
        self.adj[src].append(des)
        self.adj[des].append(src)
    
def DFS(self, start, visited):

    visited[start] = True
    for i in self.adj[start]:
        if not visited[i]:
            DFS(self, i, visited)

def isconnected(self, nmNodes):
    
    for i in range(nmNodes):
        visited = [False]*nmNodes
        DFS(self, i, visited)
        for b in visited:
            if not b:
                return False
    return True

if __name__ == "__main__":

    matrix1 = Graph(6)
    matrix1.addEdge(0, 1)
    matrix1.addEdge(1, 3)
    matrix1.addEdge(1, 5)
    matrix1.addEdge(3, 1)
    matrix1.addEdge(5, 1)



    matrix2 = Graph(6)
    matrix2.addEdge(0, 1)
    matrix2.addEdge(1, 3)
    matrix2.addEdge(1, 5)
    matrix2.addEdge(2, 3)
    matrix2.addEdge(3, 5)
    matrix2.addEdge(4, 5)
    matrix2.addEdge(5, 0)

    if isconnected(matrix1, 6) == False:
        print("Success for matrix 1")
        
    if isconnected(matrix2, 6) == True:
        print("success for matrix 2")

