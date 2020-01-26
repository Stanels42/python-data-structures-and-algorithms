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
