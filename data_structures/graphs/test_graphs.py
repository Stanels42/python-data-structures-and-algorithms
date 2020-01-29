######################
## Import Libraries ##
######################

import pytest

##################
## Import Files ##
##################

from graphs import Graph, Vertex

#################
## Test Import ##
#################

def test_imports():
  assert Graph
  assert Vertex

##########################
## Fixtures and Helpers ##
##########################

@pytest.fixture()
def sample_graph():
  g = Graph()
  v1 = g.add('Pandora')
  v2 = g.add('Arendelle')
  v3 = g.add('Metroville')
  v4 = g.add('Monstroplolis')
  v5 = g.add('Narnia')
  v6 = g.add('Naboo')

  g.add_double_edge(v1, v2, 150)
  g.add_double_edge(v1, v3, 82)
  g.add_double_edge(v2, v3, 99)
  g.add_double_edge(v2, v4, 42)
  g.add_double_edge(v3, v4, 105)
  g.add_double_edge(v3, v5, 37)
  g.add_double_edge(v3, v6, 26)
  g.add_double_edge(v4, v6, 73)
  g.add_double_edge(v5, v6, 250)

  return (g, [v1,v2,v3,v4,v5,v6])

################
## Test Graph ##
################

def test_add_vertex():
  g = Graph()
  assert g.add(10).value == 10
  assert g.add(20).value == 20

def test_same_value():
  g = Graph()
  v1 = g.add('vertex')
  v2 = g.add('vertex')
  assert not v1 == v2

def test_graph_size():
  g= Graph()
  assert g.size() == 0

  g.add(10)
  assert g.size() == 1

  g.add(20)
  assert g.size() == 2

def test_get_vertices():
  g=Graph()
  v1 = g.add('v1')
  v2 = g.add('v2')
  v3 = g.add('v3')
  v4 = g.add('v4')
  vertice_list = g.get_vertices()
  assert v1 in vertice_list
  assert v3 in vertice_list

def test_add_edge():
  g = Graph()
  v1 = g.add('v1')
  v2 = g.add('v2')
  g.add_edge(v1, v2)
  g.add_edge(v1, v2, 5)


def test_neighbors():
  g = Graph()
  v1 = g.add('v1')
  v2 = g.add('v2')
  g.add_edge(v1, v2, 5)
  assert g.get_neighbors(v1) == [(v2, 5)]
  assert g.get_neighbors(v2) == []


def test_braeth_first_single():
  """
  Test the breath first with a single value
  """
  g = Graph()
  v = g.add('v1')
  lst = g.breath_first(v)

  assert lst == ['v1']


def test_empty():
  """
  The function needs a vertex and with out any raises an error.
  """
  g = Graph()
  with pytest.raises(TypeError):
    g.breath_first()


def test_one_way():
  """
  Test the breath first can travels across the along edges
  """
  g = Graph()
  v1 = g.add('v1')
  v2 = g.add('v2')
  g.add_edge(v1, v2)
  lst_from_1 = g.breath_first(v1)
  lst_from_2 = g.breath_first(v2)
  assert lst_from_1 == ['v1', 'v2']
  assert lst_from_2 == ['v2']


def test_traverse_loop():
  """
  Test to see if the node are in a loop weather they get stuck looping over their selfs.
  """
  g = Graph()
  v1 = g.add('v1')
  v2 = g.add('v2')
  v3 = g.add('v3')
  g.add_edge(v1, v2)
  g.add_edge(v2, v3)
  g.add_edge(v3, v1)
  lst_from_1 = g.breath_first(v1)
  assert lst_from_1 == ['v1', 'v2', 'v3']


def test_braeth_first(sample_graph):

  g = sample_graph[0]
  vertices = sample_graph[1]

  lst = g.breath_first(vertices[0])

  assert lst == ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

###################
## Test Get Edge ##
###################


@pytest.mark.parametrize(
  "lst, expected",
    [
      (['Pandora'], (True, '$0')), # Not going anywhere
      (['Arendelle', 'Monstroplolis', 'Naboo'], (True, '$115')), #Across the graph
      (['Pandora', 'Arendelle', 'Monstroplolis'], (True, '$192')), # Prep test for next one
      (['Pandora', 'Arendelle', 'Monstroplolis', 'Metroville', 'Narnia', 'Naboo'], (True, '$584')), # Visit them all
      (['Monstroplolis', 'Metroville','Monstroplolis'], (True, '$210')), # Round Trip
      (['Pandora', 'Naboo'], (False, '$0')), # Skip a stop
      (['Pandora', 'Pandora'], (False, '$0')), # Going to self
      (['Mordor'], (False, '$0')), # Not in Graph
    ]
)
def test_single_value(sample_graph, lst, expected):

  g = sample_graph[0]

  actual = g.get_edge(lst)
  assert actual == expected
