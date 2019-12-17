import pytest

############################
## Import Stack And Nodes ##
############################

from node import Node
from stack import Stack, EmptyListError

##################
## Test Imports ##
##################

def test_node():
  assert Node(1)

def test_stack():
  assert Stack()

#################
## Test Stacks ##
#################

test_stack = Stack()

def test_stack_methods():
  with pytest.raises(EmptyListError):
    test_stack.peek()
  assert test_stack.is_empty()

def test_stack_enque():
  test_stack.push(1)
  assert not test_stack.is_empty()
  assert test_stack.peek() == 1
  test_stack.push(2)
  test_stack.push(3)
  test_stack.push(4)
  assert test_stack.peek() == 4

def test_deque():
  assert test_stack.pop() == 4
  assert test_stack.peek() == 3

def test_deque_all():
  test_stack.pop()
  test_stack.pop()
  test_stack.pop()
  assert test_stack.is_empty()
  with pytest.raises(EmptyListError):
    test_stack.peek()
  with pytest.raises(EmptyListError):
    test_stack.pop()
