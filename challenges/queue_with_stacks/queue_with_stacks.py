from stack import Stack, EmptyListError

class Pseudo_Queue:
  def __init__(self):
    self.stack = Stack()

  def enqueue(self, val):
    self.stack.push(val)

  def dequeue(self):
    rev_stack = Stack()
    while self.stack.top:
      rev_stack.push(self.stack.pop())
    removed = rev_stack.pop()
    while rev_stack.top:
      self.enqueue(rev_stack.pop())
    return removed
