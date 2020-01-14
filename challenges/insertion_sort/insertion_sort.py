from random import randint

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
  new_arr = []
  while len(arr) > 0:
    new_arr.append(arr.pop(randint(0, len(arr)-1)))
  return new_arr
