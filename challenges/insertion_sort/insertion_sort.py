from random import randint
from copy import deepcopy

def insertion_sort(arr):
  """
  Takes in a list and sorts the values from smallest to largest
  In: Array of intagers
  Out: Array sorted in place
  """
  for i in range(1, len(arr)):
    n = i
    while n > 0 and arr[n] < arr[n-1]:
      arr[n], arr[n-1] = arr[n-1], arr[n]
      n -= 1

def shuffle(arr):
  new_lst = deepcopy(arr)
  for i in range(len(new_lst)):
    rand = randint(i, len(new_lst) - 1)
    new_lst[i], new_lst[rand] = new_lst[rand], new_lst[i]
  return new_lst
