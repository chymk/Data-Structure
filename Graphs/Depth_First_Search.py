from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        queue = []
        visited = [None]*(len(self.graph))
        queue.append(s)
        visited[s] = True
        while queue:
            s= queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(2,0)
g.add(2,3)
g.add(3,3)

print ("Following is Breadth First Traversal starting from vertex 2",g.BFS(2))