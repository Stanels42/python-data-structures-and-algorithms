import pytest

####################
## Import Classes ##
####################

from binary_tree import BinaryTree, find_max_value
from queue import Queue

##################
## Test Imports ##
##################

def test_tree():
  assert BinaryTree()

def test_queue():
  assert Queue()

#####################
## Pytest Fixtures ##
#####################

@pytest.fixture()
def q():
  return Queue()

@pytest.fixture()
def tree():
  return BinaryTree()

################
## Test Queue ##
################

def test_enqueue(q):
  q.enqueue(10)
  assert q.peek() == 10
  assert q.dequeue() == 10
  assert q.is_empty()

######################
## Test Binary Tree ##
######################

def test_add(tree):
  tree.add('Root')
  assert tree.get_root().value == 'Root'

def test_add_multiple(tree):
  tree.add('Root')
  tree.add('Left')
  tree.add('Right')

  assert tree.get_root().value == 'Root'
  assert tree.get_root().left.value == 'Left'
  assert tree.get_root().right.value == 'Right'

def test_breath_first(tree):
  for i in range(5):
    tree.add(i)

  assert BinaryTree.breadth_first(tree) == [0,1,2,3,4]

###################
## Test Find Max ##
###################

def test_single_value(tree):
  tree.add(10)
  assert find_max_value(tree) == 10

def test_empty_tree(tree):
  assert find_max_value(tree) == None

def test_large_tree(tree):
  tree.add(1)
  tree.add(0)
  tree.add(23)
  tree.add(14)
  tree.add(56)
  tree.add(18)
  tree.add(100) # Max Value
  tree.add(34)
  tree.add(2)
  assert find_max_value(tree) == 100

def test_negitive_values(tree):
  tree.add(-1)
  tree.add(-5)
  tree.add(-23)
  tree.add(-14)
  tree.add(-56)
  tree.add(-18)
  assert find_max_value(tree) == -1
