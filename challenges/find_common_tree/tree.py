from collections import deque

class Queue:
  """
  A simple Queue class that is used by the tree to add a new value onto the tree.

  enqueue()
  In: Value
  Out: None

  dequeue()
  In: None
  Out: Value

  is_empty()
  In: None
  Out: Bool
  """
  def __init__(self):
    self.dq = deque()
  def enqueue(self, value):
    self.dq.appendleft(value)
  def dequeue(self):
    return self.dq.pop()
  def is_empty(self):
    return len(self.dq) == 0

class Tree:
  """
  Standard tree class that allows you to insert a value at the first available position

  add()
  In: Value
  Out: None
  """
  class Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
  def __init__(self):
    self.root = None

  def add(self, value):
    if not self.root:
      self.root = self.Node(value)
      return
    q = Queue()
    q.enqueue(self.root)
    while not q.is_empty():
      current = q.dequeue()
      if current.left:
        q.enqueue(current.left)
      else:
        current.left = self.Node(value)
        return
      if current.right:
        q.enqueue(current.right)
      else:
        current.right = self.Node(value)
        return
