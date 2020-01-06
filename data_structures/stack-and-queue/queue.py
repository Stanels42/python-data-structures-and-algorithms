from node import Node

class Queue:
  def __init__(self, front = None):
    """
    A constructor function that allows the user to input a another LL to create a new Queue.
    In: None or Linked List
    Exception: None
    Out: None
    """
    self.front = front
    self.end = end_next = self.front
    while end_next:
      if isinstance(end_next, Node):
        self.end = end_next
        end_next = end_next.next

  def enqueue(self, value):
    """
    Takes in a value and adds it to the end of the Queue.
    In: Value
    Exception: None
    Out: None
    """
    new_node = Node(value)
    if self.is_empty():
      self.front = self.end = new_node
    else:
      self.end.next= self.end = new_node

  def dequeue(self):
    """
    Will remove the value at the front of the Queue and return it.
    In: None
    Exception: Error if Queue is empty
    Out: Value
    """
    if self.is_empty():
      raise EmptyListError('The List is Empty')
    removed = self.front
    self.front = self.front.next
    return removed.value

  def peek(self):
    """
    Takes no input and will return the value of the first node in the Queue.
    In: None
    Exception: Error if Queue is empty
    Out: Value of first node
    """
    if not self.is_empty():
      return self.front.value
    raise EmptyListError('The List is Empty')

  def is_empty(self):
    """
    No input, returns boolean based on if there are values in the Queue
    In: None
    Exception: None
    Out: Boolean (True/False)
    """
    if self.front:
      return False
    return True

class EmptyListError(AssertionError):
  """Error for if the Queue doesn't contain any more values"""
  pass
