from collections import deque

class Queue:
  def __init__(self):
    self._dq = deque()

  def enqueue(self, value):
    self._dq.appendleft(value)

  def dequeue(self):
    return self._dq.pop()

  def peek(self):
    return self._dq[-1]

  def is_empty(self):
    return len(self._dq) == 0
