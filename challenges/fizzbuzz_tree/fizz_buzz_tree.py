from tree import BinaryTree as Tree
from node import TreeNode as _Node

def fizz_buzz_tree(tree):
  """Take in a tree of numbers and return a new tree that contains strings replacing the values of %3, %5 and %15 with Fizz, Buzz and FizzBuzz respctivly"""
  fb_tree = Tree()
  tree_root = tree.get_root()

  def recurse(tree_node, fb_node):
    """A helper function that takes in the current node and the node on the new tree and assigns the values for the new nodes"""
    if tree_node.left:
      val = fizz_or_buzz(tree_node.left.value)
      fb_node.left = _Node(val)
      recurse(tree_node.left, fb_node.left)
    if tree_node.right:
      val = fizz_or_buzz(tree_node.right.value)
      fb_node.right = _Node(val)
      recurse(tree_node.right, fb_node.right)

  def fizz_or_buzz(val):
    """A helper functio to decide if the given node should have a value of Fizz, Buzz, FizzBuzz, or to return the given value as a string"""
    result = 'Fizz' if val % 3 == 0 else ''
    result = result + 'Buzz' if val % 5 == 0 else result
    if result:
      return result
    return str(val)

  if tree_root:
    val = fizz_or_buzz(tree_root.value)
    fb_tree._root = _Node(val)
    recurse(tree_root, fb_tree._root)

  return fb_tree
