from random import randint
from copy import deepcopy

def shuffle(lst):
  """
  Takes in a list and returns a deep copy with all values in shuffled positions.
  In: List
  Out: Shuffled (new) List
  """
  new_lst = deepcopy(lst)
  for i in range(len(new_lst)):
    rand = randint(i, len(new_lst) - 1)
    new_lst[i], new_lst[rand] = new_lst[rand], new_lst[i]
  return new_lst

def merge_sort(lst):
  """
  Takes in an unsorted list and runs the merge sort algorithm to organize the values.
  In: Int List
  Out: Int List with values lowest to greatest
  """

  def recurse(lst):
    """A recursive helper function that splits a list into sublists"""
    n = len(lst)
    if n > 1:
      mid = n // 2
      left = lst[:mid]
      right = lst[mid:]

      left = recurse(left)
      right = recurse(right)

      lst = merge(left, right)
    return lst

  def merge(left, right):
    """Merges the 2 sorted lists into one larger sorted list"""
    new_lst = []
    while left and right:
      if left[0] <= right[0]:
        new_lst.append(left.pop(0))
      elif right[0] < left[0]:
        new_lst.append(right.pop(0))
    if left:
      new_lst += left
    if right:
      new_lst += right
    return new_lst

  return recurse(lst)
