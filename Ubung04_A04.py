class Graph:
     
    # init function to declare class variables
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.adj = [[] for i in range(numNodes)]
 
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def DFS(self, temp, v, visited):

        visited[v] = True
        temp.append(v)
 
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFS(temp, i, visited)
        return temp
 	
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.numNodes):
            visited.append(False)
        for v in range(self.numNodes):
            if visited[v] == False:
                temp = []
                cc.append(self.DFS(temp, v, visited))
            return cc

    def isconnected(self):
        c1 = self.connectedComponents()

        if(c1 != self):
            return False
        else:
            return True
        
        for i in range(self.numNodes):
            
 
 
# Driver Code
if __name__ == "__main__":
 
    g = Graph(6)
    g.addEdge(1, 0)
    g.addEdge(0, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 2)
    g.addEdge(5, 2)
    g.addEdge(2, 5)

    matrix2 = Graph(6)
    matrix2.addEdge(1, 0)
    matrix2.addEdge(0, 1)
    matrix2.addEdge(1, 3)
    matrix2.addEdge(3, 1)
    matrix2.addEdge(1, 5)
    matrix2.addEdge(5, 1)
    matrix2.addEdge(4, 5)
    matrix2.addEdge(5, 4)
    
    if g.isconnected() == False:
        print("success")
        
    if matrix2.isconnected() == True:
        print("success")
 
# This code is contributed by Abhishek Valsan