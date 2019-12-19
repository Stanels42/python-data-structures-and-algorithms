import pytest

##################
## Import files ##
##################

from tree import BinaryTree
from node import TreeNode
from binary_tree import BinarySearchTree

#########################
## Assert Imports Work ##
#########################

def test_node():
  assert TreeNode(1)

def test_tree():
  assert BinaryTree()

def test_B_S_tree():
  assert BinarySearchTree()

#####################
## Pytest Fixtures ##
#####################

@pytest.fixture()
def tree():
  return BinaryTree()

@pytest.fixture()
def base_tree():
  t = BinaryTree()
  t.add(1)
  t.add(2)
  t.add(3)
  return t

@pytest.fixture()
def BST():
  tree = BinarySearchTree()
  tree.add(20)
  tree.add(10)
  tree.add(30)
  tree.add(5)
  tree.add(15)
  tree.add(25)
  tree.add(35)
  return tree

###################################
## Test Adding to a Regular Tree ##
###################################

def test_add_root(tree):
  tree.add(1)
  assert tree._root.value == 1

def test_add_to_trees(tree):
  tree.add(1)
  tree.add(2)
  tree.add(3)
  assert tree._root.left.value == 2
  assert tree._root.right.value == 3

def test_pre_order(base_tree):
  assert base_tree.pre_order() == [1,2,3]

def test_in_order(base_tree):
  assert base_tree.in_order() == [2,1,3]

def test_post_order(base_tree):
  assert base_tree.post_order() == [2,3,1]

####################################
## Testing For Binary Search Tree ##
####################################

def test_bst_root(BST):
  assert BST._root.value == 20

def test_bst_root_branches(BST):
  assert BST._root.left.value == 10
  assert BST._root.right.value == 30

def test_bst_contains(BST):
  assert BST.contains(15)
  assert BST.contains(25)
  assert BST.contains(5)
  assert BST.contains(35)
  assert not BST.contains(1)

def test_empty_bst_contains():
  assert not BinarySearchTree().contains(5)

def test_bst_in_order(BST):
  assert BST.in_order() == [5,10,15,20,25,30,35]

def test_bst_in_order_again(BST):
  assert BST.in_order() == [5,10,15,20,25,30,35]
