from copy import deepcopy
from random import randint

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

def quick_sort(arr):
  """
  Takes in a list and sorts in place according to the quick sort algorithm
  In: List of numbers
  Out: Sorted list of numbers
  """
  def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
      if arr[j] < pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

  def recurse(arr, low, high):
    if low < high:
      pi = partition(arr, low, high)
      recurse(arr, low, pi-1)
      recurse(arr, pi+1, high)

  recurse(arr, 0, len(arr)-1)
