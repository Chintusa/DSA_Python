class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, directed=False):
        self.adj_matrix[u][v] = 1
        if not directed:
            self.adj_matrix[v][u] = 1

    def display(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

# Example usage
V = 4
g = Graph(V)

# Add edges (change directed=True for directed graph)
g.add_edge(0, 1)              # undirected
g.add_edge(0, 2)              # undirected
g.add_edge(1, 3, directed=True)  # directed
g.add_edge(2, 3, directed=True)  # directed

g.display()
