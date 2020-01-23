def join(left, right, join_right=False):
  """
  This function takes in 2 dictionaries. It left joins then and returns a list of tuples. Each contains the key the value from the first dictionary and if there is one, the value from the second dictionary.
  In: 2 dictionaries
  Out: Nested lists
  """
  if join_right:
    left, right = right, left
  output = []
  for key in left:
    output.append((key, left[key], right[key] if key in right else None))
  return output or None

