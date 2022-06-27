from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

        # A function that does union of two sets of x and y
        # (uses union by rank)

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalsMST(self):
        result = []
        i = 0
        # An index variable, used for sorted edges
        e = 0
        # An index used for result[]
        self.graph = sorted(self.graph, key=lambda a: a[2])
        parent,rank = [],[]
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V-1:
            u,v,w = self.graph[i]
            i = i+1
            x = self.find(parent,u)
            y = self.find(parent,v)

            if x!=y:
                e = e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)



