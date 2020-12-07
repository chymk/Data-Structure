from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCycle(self):
        visited = [False]*self.V

        for vertice in self.graph:
            if visited[vertice] == False:
                if self.isCycleUtil(vertice,visited,-1) == True:
                    return True
        return False

    def isCycleUtil(self,v,visited,parent):

        visited[v] = True
        print("List",self.graph[v])
        print("Node",v)

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCycleUtil(neighbour,visited,v) == True:
                    return True
            elif parent != neighbour  :
                return True

        return False

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)


print("Graph is Cyclic") if g.isCycle() else print("Graph is not Cyclic")

