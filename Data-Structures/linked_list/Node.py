class Node:

  def __init__(self, value = None, next_node = None):
    self._value = value
    self._next = next_node

  def __str__(self):
    return str(self._value)

  def set_value(self, value = None):
    self._value = value

  def set_next(self, next_node = None):
    if next_node == None or isinstance(next_node, Node):
      self._next = next_node
    else:
      raise TypeError

  def get_value(self):
    return self._value

  def get_next(self):
    return self._next
