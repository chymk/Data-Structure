from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self,u,v):
        self.graph[u].append(v)

    def DFS(self,s):
        visited = set()
        self.DFSUtil(s,visited)

    def DFSUtil(self,s,visited):
        visited.add(s)
        print(s,end=" ")
        for i in self.graph[s]:
            if i not in visited:
                self.DFSUtil(i,visited)


g = Graph()

g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(2,0)
g.add(2,3)
g.add(3,3)

print(g.graph)

print ("Following is Breadth First Traversal starting from vertex 2",g.DFS(2))