class Vertex:
    def __init__(self, value):
        self.value = value
class Edge:
    def __init__(self, vertex1, vertex2, value):
        self.value = value
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def end_points(self):
        return (self.vertex1, self.vertex2)

class Graph:
    def __init__(self):
        self.a = []
        self.label = None
        self.n = None
    def setAMatrix(self, b, m):