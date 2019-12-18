import pytest

############################
## Import Stack And Nodes ##
############################

from node import Node
from queue import Queue, EmptyListError

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
  with pytest.raises(EmptyListError):
    test_queue.peek()
  assert test_queue.is_empty()

def test_stack_enque():
  test_queue.enqueue(1)
  assert not test_queue.is_empty()
  assert test_queue.peek() == 1
  test_queue.enqueue(2)
  test_queue.enqueue(3)
  test_queue.enqueue(4)
  assert test_queue.peek() == 1

def test_deque():
  assert test_queue.dequeue() == 1
  assert test_queue.peek() == 2

def test_deque_all():
  test_queue.dequeue()
  test_queue.dequeue()
  test_queue.dequeue()
  assert test_queue.is_empty()
  with pytest.raises(EmptyListError):
    test_queue.peek()
  with pytest.raises(EmptyListError):
    test_queue.dequeue()
