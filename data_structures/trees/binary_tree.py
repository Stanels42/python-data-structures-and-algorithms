from node import TreeNode as _Node
from tree import BinaryTree

class BinarySearchTree(BinaryTree):

  def add(self, value, node = None):
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

# def basetree():
#   t = BinaryTree()
#   t.add(1)
#   t.add(2)
#   t.add(3)
#   return t

def B_S_T():
  tree = BinarySearchTree()
  tree.add(20)
  tree.add(10)
  tree.add(30)
  tree.add(5)
  tree.add(15)
  tree.add(25)
  tree.add(35)
  return tree

if __name__ == "__main__":
  # base_tree = basetree()
  BST = B_S_T()

  # base_tree.in_order()
  print(BST.in_order())
  print(BST.in_order())
