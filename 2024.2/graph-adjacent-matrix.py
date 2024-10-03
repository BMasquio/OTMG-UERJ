class Graph:
    def __init__(self, n_vertices=0, edges=None):
        # Initialize the graph with n vertices and optional edges
        self.n = n_vertices  # Number of vertices
        self.adj_matrix = [[0] * self.n for _ in range(self.n)]
        if edges is not None:
            for u, v in edges:
                self.add_edge(u, v)

    def input_graph(self):
        # Initialize the graph via command line input
        self.n = int(input("Enter the number of vertices: "))
        self.adj_matrix = [[0] * self.n for _ in range(self.n)]
        m = int(input("Enter the number of edges: "))
        print("Enter the edges as pairs of vertices (0-based indices):")
        for _ in range(m):
            u, v = map(int, input().split())
            self.add_edge(u, v)

    def add_vertex(self):
        # Add a new vertex to the graph
        self.n += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.n)

    def remove_vertex(self, vertex):
        # Remove a vertex and its associated edges from the graph
        if vertex < 0 or vertex >= self.n:
            print(f"Vertex {vertex} does not exist.")
            return
        # Remove the row and column corresponding to the vertex
        self.adj_matrix.pop(vertex)
        for row in self.adj_matrix:
            row.pop(vertex)
        self.n -= 1

    def add_edge(self, u, v):
        # Add an edge between two vertices
        if u < 0 or u >= self.n or v < 0 or v >= self.n:
            print(f"One or both vertices {u}, {v} do not exist.")
            return
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph

    def remove_edge(self, u, v):
        # Remove the edge between two vertices
        if u < 0 or u >= self.n or v < 0 or v >= self.n:
            print(f"One or both vertices {u}, {v} do not exist.")
            return
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0  # For undirected graph

    def neighbors(self, vertex):
        # Return the list of neighbors for a given vertex
        if vertex < 0 or vertex >= self.n:
            print(f"Vertex {vertex} does not exist.")
            return []
        return [i for i in range(self.n) if self.adj_matrix[vertex][i] != 0]

    def are_adjacent(self, u, v):
        # Check if two vertices are adjacent
        if u < 0 or u >= self.n or v < 0 or v >= self.n:
            print(f"One or both vertices {u}, {v} do not exist.")
            return False
        return self.adj_matrix[u][v] != 0

    def to_dot(self):
        # Generate DOT code for the graph with circle-shaped vertices
        dot = "graph G {\n"
        dot += "    node [shape=circle];\n"
        # Add all vertices
        for vertex in range(self.n):
            dot += f"    {vertex};\n"
        # Add all edges without duplicates
        for u in range(self.n):
            for v in range(u + 1, self.n):
                if self.adj_matrix[u][v]:
                    dot += f"    {u} -- {v};\n"
        dot += "}"
        return dot

    def print_adjacency_matrix(self):
        # Print the adjacency matrix in a formatted way with indices and big square brackets
        n = self.n
        col_width = 5  # Increase column width to make cells more sparse
        # Print column indices
        print(" " * (col_width + 2), end="")
        for j in range(n):
            print(f"{j:>{col_width}}", end="")
        print()
        # Print top bracket
        print(" " * (col_width + 1) + "┌" + "─" * (n * col_width) + "┐")
        # Print each row with row indices
        for i in range(n):
            print(f"{i:>{col_width}} │", end="")
            for j in range(n):
                print(f"{self.adj_matrix[i][j]:>{col_width}}", end="")
            print(" │")
        # Print bottom bracket
        print(" " * (col_width + 1) + "└" + "─" * (n * col_width) + "┘")


#g = Graph(4, edges=[(0, 1), (1, 2), (2, 3), (3, 0)])

# Print the adjacency matrix with more spacing
#print("Adjacency Matrix:")
#g.print_adjacency_matrix()
#print(g.to_dot()) #paste it to https://dreampuf.github.io/GraphvizOnline