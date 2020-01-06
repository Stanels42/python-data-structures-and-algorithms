def insert_shift_array(lst, val):
  """Takes in a list and a value and insertes the value in the center of the list"""
  center = (len(lst) + 1) // 2
  return lst[:center] + [val] + lst[center:]

def remove_center(lst):
  """Remove the center of a list favoring the position just left of center"""
  center = len(lst) // 2
  return lst[:center] + lst[(center+1):]
