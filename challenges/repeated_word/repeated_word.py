from re import findall

def repeated_word(string):
  """
  Take in a string and return the first repeated word. It there are no repeats then just return None
  In: String
  Out: String/None
  """
  if not isinstance(string, str):
    raise ValueError
  word_set = set()
  for word in findall(r'[A-Za-z]+\'?[a-z]*', string.lower()):
    if word in word_set:
      return word
    word_set.add(word)
  return None

def all_repeated_words(string):
  if not isinstance(string, str):
    raise ValueError
  word_set = set()
  repeated_words = set()
  for word in findall(r'[A-Za-z]+\'?[a-z]*', string.lower()):
    if word in word_set:
      repeated_words.add(word)
    word_set.add(word)
  return repeated_words or None
