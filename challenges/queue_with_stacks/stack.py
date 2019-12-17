from node import Node

class Stack:
  def __init__(self, top = None):
    self.top = top

  def push(self, value):
    new_top = Node(value, self.top)
    self.top = new_top

  def pop(self):
    if not isinstance(self.top, Node):
      raise EmptyListError
    removed = self.top
    self.top = self.top.next
    return removed.value

  def peek(self):
    if isinstance(self.top, Node):
      return self.top.value
    raise EmptyListError

  def is_empty(self):
    if self.top:
      return False
    return True

class EmptyListError(AssertionError):
  pass
