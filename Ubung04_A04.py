class Graph:
     
    # init function to declare class variables
    def __init__(self, numNodes):
        self.numNodes = numNodes
        self.adj = [[] for i in range(numNodes)]
 
    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
 
    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.numNodes):
            visited.append(False)
        for v in range(self.numNodes):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    def isconnected(self):
        c1 = self.connectedComponents()

        if(c1 != self):
            return False
        else:
            return True
        return False
 
 
# Driver Code
if __name__ == "__main__":
 
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(6)
    g.addEdge(1, 0)
    g.addEdge(0, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 2)
    g.addEdge(5, 2)
    g.addEdge(2, 5)
    cc = g.isconnected()
    print("Following are connected components")
    print(cc)
 
# This code is contributed by Abhishek Valsan