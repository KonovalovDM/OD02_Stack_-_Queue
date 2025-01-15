class Graph:
   def __init__(self):
       self.graph = {}

   def add_edge(self, u, v):
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)

   def print_graph(self):
       # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
       for node in self.graph:
           print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge(0, 3)
g.add_edge(0, 7)
g.add_edge(1, 6)
g.add_edge(1, 3)
g.add_edge(1, 9)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(3, 9)

g.print_graph()
