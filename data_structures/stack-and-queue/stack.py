from node import Node

class Stack:
  def __init__(self, top = None):
    self.top = top

  def enque(self, value):
    new_top = Node(value, self.top)
    self.top = new_top

  def deque(self):
    if not isinstance(self.top, Node):
      return 'Error'
    removed = self.top
    self.top = self.top.next
    return removed

  def peek(self):
    if isinstance(self.top, Node):
      return self.top.value
    return 'Error'

  def is_empty(self):
    if self.top:
      return False
    return True
