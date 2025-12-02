class Vertex:
  """Represents a vertex (node) in a graph."""
  def __init__(self, value):
    """Initialize the vertex with a value and an empty dictionary of edges."""
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight=0):
    """Add an edge from this vertex to another vertex with an optional weight."""
    self.edges[vertex] = weight

  def get_edges(self):
    """Return a list of vertices connected to this vertex."""
    return list(self.edges.keys())

  def edge_weight(self, edge):
    """Return the weight of the edge to the specified vertex."""
    return self.edges[edge]

class Graph:
  """Represents a graph data structure, which can be directed or undirected."""
  def __init__(self, directed=False):
    """Initialize the graph with an empty dictionary of vertices and a directed flag."""
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    """Add a vertex to the graph."""
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight=0):
    """Add an edge between two vertices with an optional weight. For undirected graphs, add edges in both directions."""
    if from_vertex.value in self.graph_dict and to_vertex.value in self.graph_dict:
      self.graph_dict[from_vertex.value].add_edge(to_vertex, weight)
      if not self.directed:
          self.graph_dict[to_vertex.value].add_edge(from_vertex, weight)
    else:
        print(f"Error: One or both vertices not found in graph.")