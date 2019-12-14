
############################
## Import Stack And Nodes ##
############################

from node import Node
from queue import Queue

##################
## Test Imports ##
##################

def test_node():
  assert Node(1)

def test_queue():
  assert Queue()

#################
## Test Stacks ##
#################

test_queue = Queue()

def test_stack_methods():
  assert test_queue.peek() == 'Error'
  assert test_queue.is_empty()

def test_stack_enque():
  test_queue.enque(1)
  assert not test_queue.is_empty()
  assert test_queue.peek() == 1
  test_queue.enque(2)
  test_queue.enque(3)
  test_queue.enque(4)
  assert test_queue.peek() == 1

def test_deque():
  assert test_queue.deque().value == 1
  assert test_queue.peek() == 2

def test_deque_all():
  test_queue.deque()
  test_queue.deque()
  test_queue.deque()
  assert test_queue.is_empty()
  assert test_queue.peek() == 'Error'
  assert test_queue.deque() == 'Error'
