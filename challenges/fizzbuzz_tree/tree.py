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


  def _default_action(self,value=None, arr=None):
    """The default action for the order functions that returns a list contains all given values of the tree"""
    arr = arr or []
    arr.append(value)
    return arr


  def pre_order(self, node=None, action=None, acc=None):
    """Display the values of a tree in self left right order"""
    action = action or self._default_action
    if not self._root:
      return action()
    node = node or self._root
    acc = action(node.value, acc)
    if node.left:
      acc = self.pre_order(node.left, action, acc)
    if node.right:
      acc = self.pre_order(node.right, action, acc)
    return acc


  def in_order(self, node=None, action=None, acc=None):
    """
    Traverse the tree in order and preform a given action on every node in the tree.
    By default it returns a list of the values in order
    """
    if action is None:
      action = self._default_action
    if not self._root:
      return action()
    node = node or self._root
    if node.left:
      acc = self.in_order(node.left, action, acc)
    acc = action(node.value, acc)
    if node.right:
      acc = self.in_order(node.right, action, acc)
    return acc


  def post_order(self, node=None, action=None, acc=None):
    """Display the values in a tree in left right self order"""
    action = action or self._default_action
    if not self._root:
      return action()
    node = node or self._root
    if node.left:
      acc = self.post_order(node.left, action, acc)
    if node.right:
      acc = self.post_order(node.right, action, acc)
    acc = action(node.value, acc)
    return acc


