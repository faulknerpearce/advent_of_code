class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight=0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

  def edge_weight(self, edge):
    return self.edges[edge]

class Graph:
  def __init__(self, directed=False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight=0):
    if from_vertex.value in self.graph_dict and to_vertex.value in self.graph_dict:
      self.graph_dict[from_vertex.value].add_edge(to_vertex, weight)
      if not self.directed:
          self.graph_dict[to_vertex.value].add_edge(from_vertex, weight)
      else:
        print(f"Error: One or both vertices not found in graph.")