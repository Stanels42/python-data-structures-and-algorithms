from Node import Node

class Linked_List:

  def __init__(self, head = None):
    """Can take in an existing """
    self.head = head
    self._length = 0


  def __str__(self):

    output = "This Linked List is " + str(self._length) + " Node(s) Long\n"

    current = self.head
    while current:
      output += str(current) + "\n"
      current = current.get_next()
    return output


  def add_to_head(self, value = None):
    """Adds a given value to the head of the linked list"""

    if not isinstance (value, Node):
      value = Node(value)

    value.set_next(self.head)
    self.head = value

    self._length += 1


  def includes(self, value):
    """Check if a linked list has a given value and retruns true or false depending on the output"""

    if not self.head:
      return False

    current = self.head

    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()

    return False


  def get_length(self):
    """Returns the current length of the linked list"""
    return self._length

