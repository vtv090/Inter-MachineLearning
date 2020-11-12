class edge:
    def __init__(self, source = 0, target = 0):
        self.source = source
        self.target = target

def getNodes(edges):
    nodes =[]
    for edge in edges:
        if edge.source not in nodes:
            nodes.append(edge.source)
        if edge.target not in nodes:
            nodes.append(edge.target)
    return nodes


def isReach(edges, s, d):
    nodes = getNodes(edges)
    visited = [False]*len(nodes)

    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        n = queue.pop()
        if n == d:
            return
        
        for i in range(len(nodes)):
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return False


def getRoot(edges):
    nodes = getNodes(edges)
    root = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if isReach(nodes, nodes[i], nodes[j]) == True:
                root.append(nodes[i])
    return root

edges = [edge(1, 3), edge(3, 4), edge(4, 5), edge(5,1), edge(5,2)]

print(getRoot(edges))