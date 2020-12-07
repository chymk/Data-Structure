from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def isCycle(self):
        visited = [False]*self.V
        recStack = [False]*self.V

        for vertice in self.graph:
            if visited[vertice] == False:
                if self.isCycleUtil(vertice,visited,recStack) == True:
                    return True
        return False

    def isCycleUtil(self,v,visited,recstack):

        visited[v] = True
        recstack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCycleUtil(v,visited,recstack) == True:
                    return True
            elif recstack[neighbour] == True:
                return True

        recstack[v] = False
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

