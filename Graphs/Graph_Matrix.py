class Graph:
    def __init__(self):
        self.graph = []
        self.verticesNum = 0
        self.vertices = []

    def add_vertex(self,v):
        if v in self.vertices:
            print("Vertex ",v," already exist")
        else:
            self.vertices.append(v)
            self.verticesNum += 1
            if self.verticesNum >1:
                for vertex in self.graph:
                    vertex.append(0)
            temp = []
            for i in range(self.verticesNum):
                temp.append(0)
            self.graph.append(temp)

    def add_edge(self,v1,v2,e):
        if v1 not in self.vertices:
            print("Vertex ",v1," doesn't exist")
        elif v2 not in self.vertices:
            print("Vertex ", v2, " doesn't exist")
        else:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.graph[index1][index2] = e

    def printGraph(self):
        for i in range(self.verticesNum):
            for j in range(self.verticesNum):
                if self.graph[i][j] != 0:
                    print(self.vertices[i],"->",self.vertices[j]," Edge Weight ",self.graph[i][j])

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_edge(1,2,1)
g.add_edge(1,3,1)
g.add_edge(2,3,3)
g.add_edge(3,4,4)
g.add_edge(4,1,5)
g.printGraph()
