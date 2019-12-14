
############################
## Import Stack And Nodes ##
############################

from node import Node
from stack import Stack

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
  assert test_stack.peek() == 'Error'
  assert test_stack.is_empty()

def test_stack_enque():
  test_stack.enque(1)
  assert not test_stack.is_empty()
  assert test_stack.peek() == 1
  test_stack.enque(2)
  test_stack.enque(3)
  test_stack.enque(4)
  assert test_stack.peek() == 4

def test_deque():
  assert test_stack.deque().value == 4
  assert test_stack.peek() == 3

def test_deque_all():
  test_stack.deque()
  test_stack.deque()
  test_stack.deque()
  assert test_stack.is_empty()
  assert test_stack.peek() == 'Error'
  assert test_stack.deque() == 'Error'
