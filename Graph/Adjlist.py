class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, directed=False):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

        if not directed:
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.adj_list[v].append(u)

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.print_graph()
