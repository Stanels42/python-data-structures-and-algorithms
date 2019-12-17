from node import Node

class Queue:
  def __init__(self, front = None):
    self.front = front
    self.end = end_next = self.front
    while end_next:
      if isinstance(end_next, Node):
        self.end = end_next
        end_next = end_next.next

  def enque(self, value):
    new_node = Node(value)
    if self.is_empty():
      self.front = self.end = new_node
    else:
      self.end.next= self.end = new_node

  def deque(self):
    if self.is_empty():
      raise EmptyListError('The List is Empty')
    removed = self.front
    self.front = self.front.next
    return removed

  def peek(self):
    if not self.is_empty():
      return self.front.value
    raise EmptyListError('The List is Empty')

  def is_empty(self):
    if self.front:
      return False
    return True

class EmptyListError(AssertionError):
  pass
