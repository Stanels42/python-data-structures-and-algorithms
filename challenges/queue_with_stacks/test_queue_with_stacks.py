import pytest

#############################
## Import Queue from Stack ##
#############################

from queue_with_stacks import Pseudo_Queue as Queue
from queue_with_stacks import EmptyListError

#############################
## Basic Queue Setup Tests ##
#############################

def test_making_queue():
  assert Queue()

##################
## Test Methods ##
##################

def test_one_value():
  queue = Queue()
  queue.enqueue(1)
  assert 1 == queue.dequeue()

def test_one_multivalues():
  queue = Queue()
  for i in range(10):
    queue.enqueue(i)
  assert 0 == queue.dequeue()
  assert 1 == queue.dequeue()
  assert 2 == queue.dequeue()


def test_dequeue_empty():
  queue = Queue()
  with pytest.raises(EmptyListError):
    queue.dequeue()
