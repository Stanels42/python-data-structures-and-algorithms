def insert_shift_array(lst, val):
  center = (len(lst) + 1) // 2
  return lst[:center] + [val] + lst[center:]

def remove_center(lst):
  center = len(lst) // 2
  return lst[:center] + lst[(center+1):]
