from Node import Node

class Linked_List:

  def __init__(self, head = None):
    """Can take in an existing linked list"""
    self.head = head
    self._length = 0


  def __str__(self):

    output = "This Linked List is " + str(self._length) + " Node(s) Long\n"

    current = self.head
    while current:
      output += str(current) + "\n"
      current = current.next
    return output


  def insert(self, value):
    """Adds a given value to the head of the linked list"""

    value = Node.is_node(value)

    value.next = self.head
    self.head = value

    self._length += 1


  def includes(self, value):
    """Check if a linked list has a given value and retruns true or false depending on the output"""

    current = self.head

    while current:
      if current.value == value:
        return True
      current = current.next

    return False


  def remove_first(self):
    """Removes the node that is positioned as the head in the linked list"""
    if not self.head:
      return

    self.head = self.head.next
    self._length -= 1


  def append(self, value):

    if not self.head:
      self.insert(value)
      return

    else:

      if not isinstance(value, Node):
        value = Node(value)

      current = self.head
      while current.next:
        current = current.next
      current.next = value
      self._length += 1


  def insert_after(self, search_value, new_value):

    current = self.head

    while current:

      if current.value == search_value:
        new_value = Node.is_node(new_value)
        new_value.next = current.next
        current.next = new_value
        self._length += 1
        return True

      current = current.next

    raise ValueError


  def insert_before(self, search_value, new_value):
    if not self.head:
      raise ValueError

    elif self.head.value == search_value:
      self.insert(new_value)
      return True

    current = self.head
    while current.next:

      if current.next.value == search_value:
        new_value = Node.is_node(new_value)
        new_value.next = current.next
        current.next = new_value
        self._length += 1
        return True

      current = current.next

    raise ValueError


  def get_length(self):
    """Returns the current length of the linked list"""
    return self._length

