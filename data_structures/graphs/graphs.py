class Graph:
  """
  Methods of graph class:

  add(value)
  - Return <Vertex>

  add_edge(<Vertex>, <Vertex>, weight=1)
  - Returns None

  size()
  returns the number of vertices in the graph, <int>

  get_vertices()
  returns list[<vertex>]

  get_neighbors(<Vertex>)
  returns a list of tuples that contain (<Vertex>, <int>:weight)
  """

  def __init__(self):
    """
    Create a new graph.
    """
    self._adjacency_list = {}

  def add(self, value):
    """
    Takes in a value and adds it to the graph
    In: Value
    Out: New Vertex
    """
    v = Vertex(value)
    self._adjacency_list[v] = []
    return v

  def add_edge(self, start, end, weight=1):
    """
    Takes in 2 vertices and an optional weight as an Int. Adds the connection from the start node to the end node.
    If either vertice is not already in the graph it raises an error.
    In: 2 vertices. Optional Weight
    Out: None
    """
    # Raise error if not in the Graph
    self.__valid_vertex(start)
    self.__valid_vertex(end)

    for edge in self._adjacency_list[start]:

      if edge == (end, int):
        edge = (end, weight)
        return

    self._adjacency_list[start].append((end, weight))


  def size(self):
    """
    Will return the number of vertices that have been added to the Graph.
    In: None
    Out: Number of vertices in the Graph
    """
    return len(self._adjacency_list)


  def get_vertices(self):
    """
    Returns a list of all vertices
    In: None
    Out: list of all vertices in the graph
    """
    return self._adjacency_list.keys()


  def get_neighbors(self, vertex):
    """
    Returns the neighbors of a given vertex.
    In: Vertex
    Out: List of edges from the vertex
    """
    # Raise error if not valid vertex
    self.__valid_vertex(vertex)
    return self._adjacency_list[vertex]


  def __valid_vertex(self, vertex):
    """
    Helper function that can check if a vertex is in the table.
    """
    if vertex not in self._adjacency_list.keys():
      raise KeyError(f'Vertex {vertex} is not in graph')
    return True

class Vertex:
  """
  A simple vertex class that is used in the graph.
  """
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return self.value
