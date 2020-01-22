def find_common(tree1, tree2):
  """
  Take in 2 binary trees and return a set of all common values in those trees.
  In: 2 Binary Trees
  Out: Set of common values
  """
  # Break if one tree is invalid
  if not tree1.root or not tree2.root:
    return None

  def recurse(current, action):
    """
    A Recursive helper function that takes in a node and action. If there is a left or right will also recurse on to the node
    """
    if current.left:
      recurse(current.left, action)
    if current.right:
      recurse(current.right, action)
    action(current)

  tree_one_set = set()
  def tree1_action(node):
    """The action to be preformed in the first Tree"""
    nonlocal tree_one_set
    tree_one_set.add(node.value)

  # Recurese through the first tree
  recurse(tree1.root, tree1_action)

  common_set = set()
  def tree2_action(node):
    """The action the preform on the second Tree"""
    nonlocal tree_one_set, common_set
    if node.value in tree_one_set:
      common_set.add(node.value)

  # Recurse through the second tree
  recurse(tree2.root, tree2_action)

  return common_set or None
