from queue import Queue
from node import TreeNode as _Node

class BinaryTree:
  def __init__(self):
    self._root = None

  def get_root(self):
    """Get the root. Serously"""
    return self._root

  def add(self, value):
    """Add a value to the base binary tree.
    If there are errors please comment out this function. I have had some troble with the queue already"""
    node = _Node(value)
    if not self._root:
      self._root = node
      return

    node_queue = Queue()
    current = self._root
    while True:
      if current.left == None:
        current.left = node
        return
      else:
        node_queue.enqueue(current.left)
      if current.right == None:
        current.right = node
        return
      else:
        node_queue.enqueue(current.right)
      current = node_queue.dequeue()

  def pre_order(self, node=None, arr=None):
    """Display the values of a tree in self left right order"""
    arr = [] if arr == None else arr
    if not self._root:
      return arr
    node = node or self._root
    arr.append(node.value)
    if node.left:
      self.pre_order(node.left, arr)
    if node.right:
      self.pre_order(node.right, arr)
    return arr



  def in_order(self, node=None, arr=None):
    """Display the values in the tree in left center self order"""
    arr = [] if arr == None else arr
    if not self._root:
      return arr
    node = node or self._root

    if node.left:
      self.in_order(node.left, arr)

    arr.append(node.value)

    if node.right:
      self.in_order(node.right, arr)

    return arr



  def post_order(self, node=None, arr=None):
    """Display the values in a tree in left right self order"""
    arr = [] if arr == None else arr
    if not self._root:
      return arr
    node = node or self._root
    if node.left:
      self.post_order(node.left, arr)
    if node.right:
      self.post_order(node.right, arr)
    arr.append(node.value)
    return arr
