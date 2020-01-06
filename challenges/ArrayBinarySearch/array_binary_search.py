# Worked in Repl.it
# def binary_search_recursive(arr, val, left = 0, right = len(arr)):
#   mid = (right + left) // 2
#   if right <= left:
#     return -1
#   elif val > arr[mid]:
#     return binary_seach(arr, val, mid, right)
#   elif val < arr[mid]:
#     return binary_seach(arr, val, left, mid)
#   else:
#     return mid

def binary_search(arr, val):
  """Takes in a sorted list and a value. Preforms the Binary Search algorythem to see if the value is in the lsit."""
  # Set the values to the end of the list
  left,right = 0,len(arr)

  while not right <= left:

    mid = (right + left) // 2

    if val > arr[mid]:
      left = mid+1
    elif val < arr[mid]:
      right = mid
    else:
      return mid

  return -1
