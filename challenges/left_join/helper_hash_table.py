class LinkedList:

  class Node:
    def __init__(self, key, value):
      self.value = value
      self.key = key
      self.next = None


  def __init__(self):
    self.root = None


  def add(self, key, value):

    if not self.root:
      self.root = self.Node(key, value)
      return

    current = self.root
    while current.next:
      current = current.next
    current = self.Node(key, value)


  def replace(self, key, value):
    current = self.root
    while not current.key == key:
      current = current.next
    current.value = value


  def get(self, key):
    current = self.root
    while current:
      if current.key == key:
        return current.value
      current = current.next

class HashTable:

  def __init__(self, length=64):
    self.length = length
    self.keys = set()
    self.table = [None] * length


  def add(self, key, value):
    if key in self.keys:
      self.replace(key, value)
    index = self._hash(key)
    if self.table[index] == None:
      self.table[index] = LinkedList()
    self.table[index].add(key, value)
    self.keys.add(key)


  def replace(self, key, value):
    if not key in self.keys:
      self.add(key, value)
    index = self._hash(key)
    self.table[index].replace(key, value)
    self.keys.add(key)


  def contains(self, key):
    return key in self.keys


  def get(self, key):
    index = self._hash(key)
    return self.table[index].get(key)


  def _hash(self, key):
    key_sum=0
    for char in key:
      key_sum += ord(char)
    key_sum *= 521
    return key_sum % self.length


  def __getitem__(self, key):
    if key in self.keys:
      return self.get(key)
    return None

  def __setitem__(self, key, value):
    self.add(key, value)

  def __len__(self):
    return len(self.keys)

  def __iter__(self):
    class IT:
      def __init__(self, keys):
        self.keys = list(keys)
        self.index = -1

      def __next__(self):
        self.index += 1
        if self.index >= len(self.keys):
          raise StopIteration
        return self.keys[self.index]
    return IT(self.keys)
