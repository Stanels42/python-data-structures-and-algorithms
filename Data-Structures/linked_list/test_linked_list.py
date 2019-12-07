##
import pytest

## Import Classes ##

from Node import Node
from linked_list import Linked_List


##########################
## Creating Linked List ##
##########################

def test_create_node():
  assert isinstance(Node(), Node)

def test_new_linked_list(test_list):
  assert isinstance(test_list, Linked_List)

def test_add_values_to_list(test_list):
  test_list.add_to_head(Node())
  assert test_list.get_length() == 1
  test_list.add_to_head(Node())
  test_list.add_to_head(Node())
  assert test_list.get_length() == 3

#########################
## Test Node Functions ##
#########################

def test_get_value_none():
  test_node = Node()
  assert None == test_node.get_value()

def test_get_value_true():
  test_node = Node(True)
  assert test_node.get_value()

def test_get_value_object():
  test_obj = Node(12)
  test_node = Node(test_obj)
  assert test_obj == test_node.get_value()

def test_set_value():
  test_node = Node()
  test_node.set_value(12)
  assert test_node.get_value() == 12

def test_set_value_string():
  test_node = Node()
  test_node.set_value(12)
  assert test_node.get_value() == 12

def test_set_value_object():
  test_node = Node()
  test_node.set_value(Node())
  assert isinstance(test_node.get_value(), Node)

def test_get_next_node_none():
  test_node = Node()
  assert test_node.get_next() == None


def test_get_next_node_node():
  test_node = Node()
  test_node.set_next(Node())
  assert isinstance(test_node.get_next(), Node)

def test_set_next_error():
  test_node = Node()
  with pytest.raises(TypeError):
    test_node.set_next('The letter 12')

########################
## Search Linked List ##
########################

def test_includes_value_true(test_list):
  for i in range(0,10):
    test_list.add_to_head(Node(i))
  assert test_list.includes(5)

def test_includes_value_false(test_list):
  for i in range(0,10):
    test_list.add_to_head(Node(i))
  assert not test_list.includes(50)

def test_includes_string(test_list):
  values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
  for char in values:
    test_list.add_to_head(char)
  assert test_list.includes('f')

###########################
## Print the Linked List ##
###########################

def test_print_empty_list(test_list):
  expected = """This Linked List is 0 Node(s) Long\n"""
  assert expected == str(test_list)

def test_print_filled_list(test_list):
  expected = """This Linked List is 2 Node(s) Long
2
1
"""
  test_list.add_to_head(1)
  test_list.add_to_head(2)
  assert expected == str(test_list)


###############
## Test List ##
###############

@pytest.fixture()
def test_list():
  return Linked_List()
