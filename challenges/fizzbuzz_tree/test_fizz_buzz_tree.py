import pytest

##################
## Import files ##
##################

from tree import BinaryTree
from node import TreeNode
from fizz_buzz_tree import fizz_buzz_tree

#########################
## Assert Imports Work ##
#########################

def test_imports():
  assert BinaryTree()
  assert TreeNode(1)

#####################
## Pytest Fixtures ##
#####################

@pytest.fixture()
def test_tree():
  tree = BinaryTree()
  tree.add(3)
  tree.add(5)
  tree.add(15)
  tree.add(2)
  tree.add(8)
  return tree

#####################
## Fizz Buzz Tests ##
#####################

def test_empty_tree():
  tree = BinaryTree()
  assert fizz_buzz_tree(tree)._root == None

def test_one_value():
  tree = BinaryTree()
  tree.add(1)
  fb_tree = fizz_buzz_tree(tree)
  expected = ['1']
  actual = fb_tree.in_order()
  assert expected == actual

def test_Fizz():
  tree = BinaryTree()
  tree.add(9)
  fb_tree = fizz_buzz_tree(tree)
  assert fb_tree.in_order() == ['Fizz']

def test_Buzz():

  tree = BinaryTree()
  tree.add(10)
  fb_tree = fizz_buzz_tree(tree)
  assert fb_tree.in_order() == ['Buzz']


def test_FizzBuzz():
  tree = BinaryTree()
  tree.add(45)
  fb_tree = fizz_buzz_tree(tree)
  assert fb_tree.in_order() == ['FizzBuzz']


def test_populated_tree(test_tree):
  result = fizz_buzz_tree(test_tree)
  actual = result.in_order()
  expected = ['2','Buzz','8','Fizz','FizzBuzz']
  assert actual == expected

def test_string_in_tree():
  """The tree can only handle numbers. Strings will throw an error"""
  tree = BinaryTree()
  tree.add('15')
  with pytest.raises(TypeError):
    fizz_buzz_tree(tree)
