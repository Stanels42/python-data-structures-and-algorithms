from node import Node

class Stack:
  def __init__(self, top = None):
    self.top = top

  def push(self, value):
    """Add a given value to the top of the stack.
    In: Value
    Exceptions: None
    Out: None"""
    new_top = Node(value, self.top)
    self.top = new_top

  def pop(self):
    """Remove the first value from the stack and return it
    In: None
    Exciptions: Error if empty List
    Out: The removed value"""
    if not isinstance(self.top, Node):
      raise EmptyListError
    removed = self.top
    self.top = self.top.next
    return removed.value

  def peek(self):
    """Look at the top value from the stack and return it
    In: None
    Exciptions: Error if empty Stack
    Out: The top value"""
    if isinstance(self.top, Node):
      return self.top.value
    raise EmptyListError

  def is_empty(self):
    """Function that returns a boolian based on if the stack contains any values.
    In: None
    Exceptions: None
    Out: Boolean (True/False)"""
    if self.top:
      return False
    return True

class EmptyListError(AssertionError):
  pass
