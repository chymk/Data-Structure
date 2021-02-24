class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices_Num = 0

    def add_vertices(self,v):
        if v in self.graph:
            print("Vertex ",v," already exist")
        else:
            self.vertices_Num += 1
            self.graph[v] = []

    def add_edges(self,v1,v2,e):
        if v1 not in self.graph:
            print("Vertex",v1," doesn't exist")
        if v2 not in self.graph:
            print("vertex", v2," doesn't exist")
        else:
            temp = [v2,e]
            self.graph[v1].append(temp)

    def printGraph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(vertex,"->",edges[0]," edge weight",edges[1])
g = Graph()
g.add_vertices(1)
g.add_vertices(2)
g.add_vertices(3)
g.add_vertices(4)

g.add_edges(1,2,1)
g.add_edges(1,3,1)
g.add_edges(2,3,3)
g.add_edges(3,4,4)
g.add_edges(4,1,5)
print(g.graph)

g.printGraph()


