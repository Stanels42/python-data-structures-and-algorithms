from collections import deque

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

  def add_edge(self, start, end, weight=0):
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
    Returns a list of all vertices.
    In: None
    Out: list of all vertices in the graph
    """
    return list(self._adjacency_list.keys())


  def get_neighbors(self, vertex):
    """
    Returns the neighbors of a given vertex.
    In: Vertex
    Out: List of edges from the vertex
    """
    # Raise error if not valid vertex
    self.__valid_vertex(vertex)
    return self._adjacency_list[vertex]


  def breath_first(self, vertex):
    """
    Traverse breath first form a given vertex
    In: Vertex
    Out: List of values that can be accessed through the graph.
    """
    output = []

    def action(vertex):
      output.append(vertex.value)

    self.__traverse(vertex, action)

    return output


  def depth_first(self, vertex):
    """
    Traverse the tree in depth first order adding the value of each vertex to the output list.
    In: <Vertex>
    Out: <list> of values
    """
    output = []

    def action(vertex):
      output.append(vertex.value)

    self.__recurse(vertex, action)

    return output


  def add_double_edge(self, vertex1, vertex2, weight=0, weight2=None):
    """
    Similar to add edge just adds it adds one going both ways.
    In: 2 vertices and a weight
    Out: None
    """
    weight2 = weight if weight2 == None else weight2 or 0
    self.add_edge(vertex1, vertex2, weight)
    self.add_edge(vertex2, vertex1, weight2)


  def get_edge(self, v_lst):
    """
    Takes in a list of values in the graph and retruns the True or False on if you can fallow all the Vertices and the sum of the weight when traveling between them.
    In: List of values contained in the vertices.
    Out: tuple(True/False, sum <int>)
    """

    def contains_vertex(value, lst):
      """Helper function for the get edge method that can find it the string value is a value of a neighbor node"""
      for vertex in lst:
        # Used when looking at the list of edges for a vertex
        if isinstance(vertex, Vertex):
          if vertex.value == value:
            return vertex
        # Used when trying to see if the vertex is in the graph at all.
        elif vertex[0].value == value:
          return vertex
      # Need to return the value and price for the inner loop
      return False, 0

    # Check if the first value is the value of a vertex in the graph.
    current = contains_vertex(v_lst[0], self.get_vertices())
    if isinstance(current, Vertex):
      travel_sum = 0
      # Ignore the first position because it's handeled above
      for index in range(1,len(v_lst)):
        # See if the next value is a neighbor and get the weight of the connection.
        current,cost = contains_vertex(v_lst[index], self.get_neighbors(current))
        travel_sum += cost
        # Current is False if the vertex is not a neighbor of the current Vertex
        if not current:
          return (False, '$0')
      # If the entire list is traversed with out fail return True and the sum of all edges
      return (True, f'${str(travel_sum)}')
    # If vertex not in graph return false
    return (False, '$0')


  def __traverse(self, vertex, action):
    """
    Takes in a starting vertex and an action. Will traverse the graph in a breath first order from the given vertex. The action is a function that is acted on each vertex.
    """
    self.__valid_vertex(vertex)

    q = Queue()
    q.enqueue(vertex)
    visited = set([vertex])

    while not q.empty():
      current = q.dequeue()

      for vert in self.get_neighbors(current):
        vert = vert[0]
        if vert not in visited:
          visited.add(vert)
          q.enqueue(vert)

      action(current)


  def __recurse(self, vertex, action):
    """
    A recursive helper function that takes a starting vertex and action. Then traverses the graph in an in order manner applying the action the current vertex.
    """
    visited = set()

    def recurse(vertex, action):

      visited.add(vertex)
      action(vertex)

      for vert in self.get_neighbors(vertex):
        if vert[0] not in visited:
          recurse(vert[0], action)

    recurse(vertex, action)


  def __valid_vertex(self, vertex):
    """
    Helper function that can check if a vertex is in the table.
    """
    if vertex not in self._adjacency_list.keys():
      raise KeyError(f'Vertex {vertex} is not in graph')
    return True


  def __len__(self):
    return len(self._adjacency_list)


##################
## Vertex Class ##
##################

class Vertex:
  """
  A simple vertex class that is used in the graph.
  """
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return self.value


#################
## Queue Class ##
#################

class Queue:
  """
  Queue class used in the implamentation of the breath first traversal
  """
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()

  def empty(self):
    return len(self.dq) == 0

class Stack:
  """Stack class for the implamentation of the depth first"""
  def __init__(self):
    self.dq = deque()

  def push(self, value):
    self.dq.append(value)

  def pop(self):
    return self.dq.pop()

  def empty(self):
    return len(self.dq) == 0
