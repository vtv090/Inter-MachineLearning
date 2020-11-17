# Python Program to check whether a graph is tree or not 
# Author: Trung Vo | vtvo90@outlook.com

class Graph: 
  
    def __init__(self, size): 
        self.size = size
        #self.adj  = defaultdict(list)
        self.adj = [[] for i in range(size)]

    
    #add Edges for undirected Graph
    def addEdge(self, src, des): 
        self.adj[src].append(des)  
        self.adj[des].append(src)  

    def isCyclicUtil(self, start, visited, parent): 
  
        visited[start] = True
        for i in self.adj[start]: 

            if visited[i] == False: 
                if self.isCyclicUtil(i, visited, start) == True: 
                    return True
            elif i != parent: 
                return True
  
        return False
  

    def isTree(self): 
        visited = [False] * self.size 
        if self.isCyclicUtil(0, visited, -1) == True: 
            return False
  
        for i in range(self.size): 
            if visited[i] == False: 
                return False
  
        return True
  
g1 = Graph(5) 
g1.addEdge(1, 0) 
g1.addEdge(0, 2) 
g1.addEdge(0, 3) 
g1.addEdge(3, 4) 
if g1.isTree() == True:
    print ("Graph is a Tree")
else:
    print ("Graph is a not a Tree")
  
g2 = Graph(5) 
g2.addEdge(1, 0) 
g2.addEdge(0, 2) 
g2.addEdge(2, 1) 
g2.addEdge(0, 3) 
g2.addEdge(3, 4) 
if g2.isTree() == True:
    print ("Graph is a Tree")
else:
    print ("Graph is a not a Tree")