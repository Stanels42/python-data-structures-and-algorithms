from node import TreeNode as _Node
from tree import BinaryTree

class BinarySearchTree(BinaryTree):

  def add(self, value, node = None):
    """Add a node to a tree based on it's value"""
    if not self._root:
      self._root = _Node(value)
      return

    node = node or self._root

    if value < node.value:
      if node.left:
        self.add(value, node.left)
      else:
        node.left = _Node(value)
    else:
      if node.right:
        self.add(value, node.right)
      else:
        node.right = _Node(value)


  def contains(self, value, node = None):
    """Find a node on a given tree in O(h) time"""
    if not self._root:
      return False

    node = node or self._root

    if node.value == value:
      return True

    if value < node.value:
      if node.left:
        return self.contains(value, node.left)
      else:
        return False
    else:
      if node.right:
        return self.contains(value, node.right)
      else:
        return False
