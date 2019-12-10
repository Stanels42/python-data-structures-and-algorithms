## Removed the private variables, because while I would like to use them, I belive that they were makeing the code more clutterend and in the end harder to read.

class Node:

  def __init__(self, value = None, next_node = None):
    self.value = value
    self.next = next_node

  def __str__(self):
    return str(self.value)

  @staticmethod
  def is_node(value, next_node = None):
    if not isinstance(value, Node):
      return Node(value, next_node)
    return value
