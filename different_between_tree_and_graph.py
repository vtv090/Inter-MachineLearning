
from collections import defaultdict 
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.adj  = defaultdict(list) 
  
    def addEdge(self, v, w): 
        # Add w to v ist. 
        self.graph[v].append(w)  
        # Add v to w list. 
        self.graph[w].append(v)  

    def isCyclicUtil(self, v, visited, parent): 
  
        # Mark current node as visited 
        visited[v] = True
  
        # Recur for all the vertices adjacent  
        # for this vertex 
        for i in self.graph[v]: 
            # If an adjacent is not visited,  
            # then recur for that adjacent 
            if visited[i] == False: 
                if self.isCyclicUtil(i, visited, v) == True: 
                    return True
  
            # If an adjacent is visited and not  
            # parent of current vertex, then there  
            # is a cycle. 
            elif i != parent: 
                return True
  
        return False
  
    def isTree(self): 

        visited = [False] * self.V 
 
        if self.isCyclicUtil(0, visited, -1) == True: 
            return False
  
        for i in range(self.V): 
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
