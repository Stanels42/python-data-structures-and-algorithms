from queue import Queue

class BinaryTree:

  class _Node:
    def __init__(self, value):
      self.value = value
      self.left = self.right = None


  def __init__(self):
    self._root = None


  def add(self, value):
    """Takes a value as an input and adds it to the binary tree in the first avliable position"""

    node = BinaryTree._Node(value)

    if self._root == None:
      self._root = node
      return

    q = Queue()
    q.enqueue(self._root)

    while True:
      current = q.dequeue()
      if current.left:
        q.enqueue(current.left)
      else:
        current.left = node
        break
      if current.right:
        q.enqueue(current.right)
      else:
        current.right = node
        break


  def get_root(self):
    """Return the current node at the root of the tree"""
    return self._root


  @staticmethod
  def breadth_first(tree):
    """Returns a list of the values in the tree in breadth first order"""

    if not tree.get_root():
      return []

    lst = []
    q = Queue()
    q.enqueue(tree.get_root())

    while not q.is_empty():
      current = q.dequeue()

      if current.left:
        q.enqueue(current.left)
      if current.right:
        q.enqueue(current.right)

      lst.append(current.value)

    return lst


def find_max_value(tree):
  """Takes in a tree and returns a max value with in the tree."""
  if not tree.get_root():
    return None
  q = Queue()
  q.enqueue(tree.get_root())
  max_val = tree.get_root().value
  while not q.is_empty():
    current = q.dequeue()
    if current.left:
      q.enqueue(current.left)
    if current.right:
      q.enqueue(current.right)
    max_val = current.value if current.value > max_val else max_val
  return max_val

def find_max_recursive(tree):
  """"""

  def recurse(current):
    max_val = current.value
    if current.left:
      left_max = recurse(current.left)
      max_val = left_max if left_max > max_val else max_val
    if current.right:
      right_max = recurse(current.right)
      max_val = right_max if right_max > max_val else max_val
    return max_val

  if not tree.get_root():
    return None
  return recurse(tree.get_root())
