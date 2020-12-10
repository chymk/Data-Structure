from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add(self,u,v):
        self.graph[u].append(v)


    def topologySort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologySortHelper(i, visited, stack)

        print(stack[::-1])


    def topologySortHelper(self,v,visited,stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologySortHelper(i, visited, stack)
        stack.append(v)

g= Graph(6)

g.add(2,3)
g.add(3,1)
g.add(4,0)
g.add(4,1)
g.add(5,2)
g.add(5,0)


print(g.graph)

print("Following is a Topological Sort of the given graph")
g.topologySort()


