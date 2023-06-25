class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex1, vertex2, value):
        self.value = value
        self.vertex1 = vertex1
        self.vertex2 = vertex2

class Graph:
    def __init__(self):
        self.adj_dict = {}
        self.a = []
        self.label = None
        self.n = None

    def setAMatrix(self, b, m):
        self.a = b
        self.n = m

    def setLabel(self, c):
        self.label = c

    def load_file(self, file_name='text_graph.txt'):
        with open(file_name, 'r') as file:
            file = file.readlines()
            label = file[0].strip().split(' ')
            matrix = []
            for row in file[1:]:
                matrix.append(row[2:].strip().split(' '))

            self.setAMatrix(matrix, len(label))
            self.setLabel(label)

    def build_graph(self, file_name='text_graph.txt'):
        self.load_file(file_name)

        num_nodes = self.n
        for label in self.label:
            self.add_vertex(label)

        # Add edges to the graph based on the adjacency matrix
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if self.a[i][j] == '1':
                    self.add_edge(self.label[i], self.label[j])

    def add_vertex(self, vertex):
        if vertex not in self.adj_dict:
            self.adj_dict[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.adj_dict:
            self.add_vertex(v1)
        if v2 not in self.adj_dict:
            self.add_vertex(v2)
        self.adj_dict[v1].add(v2)
        self.adj_dict[v2].add(v1)

    def bfs(self, start):
        if start not in self.adj_dict.keys():
            print('Input Error')

        else:
            visited = set()
            queue = [start]
            while queue:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    print(vertex, end=' ')
                    for neighbor in self.adj_dict[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)

    def dfs_recur(self, start, visited):
        # Mark the current node as visited
        visited.add(start)
        print(start, end=' ')

        # Recur for all the adjacent nodes that are not yet visited
        for neighbor in self.adj_dict[start]:
            if neighbor not in visited:
                self.dfs_recur(neighbor, visited)

    def dfs(self, start):
        if start not in self.adj_dict.keys():
            print('Input Error')

        else:
            visited = set()
            return self.dfs_recur(start, visited)

    def assign_colors(self):
        # initialize all vertices with -1 color (unassigned)
        vertex_colors = [-1] * self.n

        # iterate through all vertices
        for i in range(self.n):
            # find all adjacent vertices to the current vertex
            adjacent_colors = set()
            adjacent_vertices = self.adj_dict[self.label[i]]

            # check colors assigned to adjacent vertices
            for j in adjacent_vertices:
                if vertex_colors[self.label.index(j)] != -1:
                    adjacent_colors.add(vertex_colors[self.label.index(j)])

            # assign the first available color (i.e. the lowest non-negative integer)
            color = 0
            while True:
                if color not in adjacent_colors:
                    break
                color += 1

            vertex_colors[i] = color

        return vertex_colors


class Wgraph:
    def __init__(self):
        self.graph_dict = {}

    def add(self, node1, node2, weight):
        if node1 not in self.graph_dict:
            self.graph_dict[node1] = {}
        self.graph_dict[node1][node2] = weight

        if node2 not in self.graph_dict:
            self.graph_dict[node2] = {}
        self.graph_dict[node2][node1] = weight

    def get_nodes(self):
        return self.graph_dict.keys()

    def get_edges(self):
        edges_list = []
        for node1 in self.graph_dict:
            for node2 in self.graph_dict[node1]:
                edge_weight = self.graph_dict[node1][node2]
                edges_list.append((node1, node2, edge_weight))
        return edges_list

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph_dict}
        distances[start] = 0
        unvisited = list(self.graph_dict.keys())

        while unvisited:
            current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
            unvisited.remove(current_vertex)

            if distances[current_vertex] == float('inf'):
                break

            for neighbor, weight in self.graph_dict[current_vertex].items():
                distance = distances[current_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances

    def prim_jarnik_mst(self):
        # Initialize the MST and the set of visited vertices
        mst = []
        visited = set()

        # Choose an arbitrary starting vertex
        start_vertex = next(iter(self.graph_dict))
        visited.add(start_vertex)

        # Add all edges connected to the starting vertex to a list
        edges = [(weight, start_vertex, neighbor) for neighbor, weight in self.graph_dict[start_vertex].items()]

        # Loop until all vertices have been visited
        while edges:
            # Get the edge with minimum weight from the list
            min_edge = min(edges)
            edges.remove(min_edge)

            weight, vertex1, vertex2 = min_edge

            # Check if adding this edge will create a cycle
            if vertex2 not in visited:
                visited.add(vertex2)
                mst.append((vertex1, vertex2, weight))

                # Add all edges connected to the new vertex to the list
                for neighbor, weight in self.graph_dict[vertex2].items():
                    if neighbor not in visited:
                        edges.append((weight, vertex2, neighbor))

        return mst

g = {'A': {'D': 1, 'B': 2, 'C': 3},
     'B': {'D': 2, 'C': 1, 'A': 2},
     'C': {'D': 4, 'B': 1, 'A': 2},
     'D': {'B': 2, 'C': 4, 'A': 1, 'F': 3},
     'E': {'F': 5, 'G': 2},
     'F': {'D': 3, 'E': 5},
     'G': {'H': 1, 'I': 2, 'E': 2},
     'H': {'G': 1},
     'I': {'G': 2}}

gr = Wgraph()
gr.graph_dict = g
print(gr.dijkstra('A'))

