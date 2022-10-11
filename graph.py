class Graph:
    def __init__(self, graph_dict: dict = None) -> None:
        self.graph = graph_dict if graph_dict is not None else dict()

    def print_neighbors(self, vertex):
        return self.graph[vertex]

    def get_all_vertices(self):
        return set(self.graph.keys())

    def get_all_edges(self):
        return self._find_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            return vertex
        print("Node already in the graph")
        return None
    
    def add_edge(self, n1, n2, two_way=True):
        
        if n1 in self.graph:
            self.graph[n1].append(n2)
        else:
            self.graph[n1] = [n2]

        if two_way:
            if n2 in self.graph:
                self.graph[n2].append(n1)
            else:
                self.graph[n2] = [n1]

    def _find_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                edges.append((vertex, neighbor))

        return edges

    def __iter__(self):
        self._iterator = iter(self.graph)
        return self._iterator
    
    def __next__(self):
        return next(self._iterator)
