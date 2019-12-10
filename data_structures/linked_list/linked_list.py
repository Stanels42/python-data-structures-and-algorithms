from Node import Node

class Linked_List:

  def __init__(self, head = None):
    """Can take in an existing linked list"""
    self.head = head
    self._length = 0


  def __str__(self):

    output = "This Linked List is " + str(self._length) + " Node(s) Long\nHead->"

    current = self.head
    while current:
      output += "[" + str(current) + "]->"
      current = current.next
    return output + 'x'


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
    """Takes in a value and adds it to the end of the list"""

    if not self.head:
      return self.insert(value)

    value = Node.is_node(value)

    current = self.head
    while current.next:
      current = current.next
    current.next = value
    self._length += 1


  def insert_after(self, search_value, new_value):
    """Takes in a search value and a new value to create a new node with. If the list contains the search value the new node is inserted after that value. Otherwise raise an error"""

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
    """Takes in a search term and a new value. If the list contains the search term it will insert a new node infront of it. Otherwise raise an error"""

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


  def kth_from_end(self, k):
    """Takes in an index in the list and returns the value of the node in that position from the end. If no value is found an error is raised"""
    end = current = self.head
    count = 0
    while end:
      current = current.next if count > k else current
      end = end.next
      count += 1
    if count > k:
      return current.value
    raise ValueError


  def get_length(self):
    """Returns the current length of the linked list"""
    return self._length

