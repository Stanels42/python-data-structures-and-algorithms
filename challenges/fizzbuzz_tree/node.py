
class TreeNode:
  """The type of node that can be found growing on trees"""
  def __init__(self, val, left = None, right = None):
    self.value = val
    self.left = left
    self.right = right

class Node:
  """Compared to the treenode these tend to grow underground instead"""
  def __init__(self, val, next_ = None):
    self.value = val
    self.next = next_
