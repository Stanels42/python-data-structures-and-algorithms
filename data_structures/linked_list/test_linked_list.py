
import pytest

## Import Classes ##

from Node import Node
from linked_list import Linked_List


##########################
## Creating Linked List ##
##########################

def test_create_node():
  assert isinstance(Node(), Node)

def test_new_linked_list(empty_list):
  assert isinstance(empty_list, Linked_List)

def test_add_values_to_list(empty_list):
  empty_list.insert(Node())
  assert empty_list.get_length() == 1
  empty_list.insert(Node())
  empty_list.insert(Node())
  assert empty_list.get_length() == 3

#########################
## Test Node Functions ##
#########################

def test_get_value_none():
  test_node = Node()
  assert None == test_node.value

def test_get_value_true():
  test_node = Node(True)
  assert test_node.value

def test_get_value_object():
  test_obj = Node(12)
  test_node = Node(test_obj)
  assert test_obj == test_node.value


def test_get_next_node_none():
  test_node = Node()
  assert test_node.next == None


def test_get_next_node_node():
  test_node = Node()
  test_node.next = Node()
  assert isinstance(test_node.next, Node)

########################
## Search Linked List ##
########################

def test_includes_value_true(pop_list):
  assert pop_list.includes(5)

def test_includes_value_false(pop_list):
  assert not pop_list.includes(50)

def test_includes_string(empty_list):
  values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
  for char in values:
    empty_list.insert(char)
  assert empty_list.includes('f')

###########################
## Print the Linked List ##
###########################

def test_print_empty_list(empty_list):
  expected = """This Linked List is 0 Node(s) Long\nHead->x"""
  assert expected == str(empty_list)

def test_print_filled_list(empty_list):
  expected = """This Linked List is 2 Node(s) Long
Head->[2]->[1]->x"""
  empty_list.insert(1)
  empty_list.insert(2)
  assert expected == str(empty_list)


####################
## Removing Nodes ##
####################

def test_remove_from_empty(empty_list):
  assert not empty_list.remove_first()

def test_remove_first(empty_list):
  empty_list.insert(1)
  empty_list.insert(2)
  empty_list.insert(3)
  assert 3 == empty_list.get_length()
  assert 3 == empty_list.head.value

  empty_list.remove_first()
  assert 2 == empty_list.get_length()
  assert 2 == empty_list.head.value


##################
## Test Inserts ##
##################

def test_append_empty(empty_list):
  empty_list.append(12)
  assert empty_list.includes(12)


def test_append_end(pop_list):
  base_length = pop_list.get_length()
  pop_list.append(50)
  assert pop_list.includes(50)
  assert pop_list.get_length() == base_length + 1


def test_insert_before_front(empty_list):
  empty_list.append(2)
  empty_list.insert_before(2,1)
  assert empty_list.get_length() == 2
  assert empty_list.head.value == 1

def test_insert_before_middle(pop_list):
  pop_list.insert_before(5, 50)
  assert pop_list.includes(50)

def test_insert_before_empty(empty_list):
  with pytest.raises(ValueError):
    empty_list.insert_before(3,5)

def test_insert_before_not_found(pop_list):
  with pytest.raises(ValueError):
    pop_list.insert_after(20,3)


def test_insert_after_front(empty_list):
  empty_list.insert(1)
  assert empty_list.insert_after(1, 2)
  assert empty_list.includes(2)

def test_insert_after_middle(pop_list):
  assert pop_list.includes(5)
  pop_list.insert_after(5,50)
  assert pop_list.includes(50)

def test_insert_after_empty(empty_list):
  with pytest.raises(ValueError):
    empty_list.insert_after(3,5)

def test_insert_after_not_found(pop_list):
  with pytest.raises(ValueError):
    pop_list.insert_after(50,15)

###############
## Test List ##
###############

@pytest.fixture()
def empty_list():
  return Linked_List()

@pytest.fixture()
def pop_list():
  ll = Linked_List()
  for i in range(0, 6):
    ll.insert(i)
  return ll
