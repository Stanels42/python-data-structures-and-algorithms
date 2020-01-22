######################
## Import Libraries ##
######################

import pytest

##################
## Import Files ##
##################

from tree import Tree
from common_tree import find_common

##################
## Test Imports ##
##################

def test_import_tree():
  assert Tree

def test_function_import():
  assert find_common

###################################
## Fixtures and Helper Functions ##
###################################

def number_tree(step = 1, _range = 10, offset = 0):
  t = Tree()
  for i in range(_range):
    t.add(i * step + offset)
  return t

def string_tree(step = 1, _range = 10, offset = 0):
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  t = Tree()
  for i in range(_range):
    t.add(letters[(i * step + offset) % len(letters)])
  return t

####################
## Test Functions ##
####################

@pytest.mark.parametrize(
  "t1, t2, result",
    [
      (number_tree(), number_tree(), {0,1,2,3,4,5,6,7,8,9}),
      (number_tree(), number_tree(step=2), {0,2,4,6,8}),
      (number_tree(step=3), number_tree(step=2, _range=20), {0,6,12,18,24}),
      (string_tree(_range=2, offset=2), string_tree(offset=1), {'c','d'}),
      (number_tree(), Tree(), None),
      (number_tree(), string_tree(), None),
      (number_tree(step=0, offset=1), number_tree(step=0, offset=2), None),
      (number_tree(offset=10), number_tree(), None),
    ]
)
def test_common_tree_values(t1, t2, result):
  assert find_common(t1, t2) == result
