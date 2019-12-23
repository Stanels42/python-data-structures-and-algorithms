from pet import Cat, Dog
from queue import Queue, EmptyListError

class AnimalShelter:
  def __init__(self):
    self.queue = Queue()


  def enqueue(self, pet):
    if isinstance(pet, Cat) or isinstance(pet, Dog):
      self.queue.enqueue(pet)


  def dequeue(self, pet_type):
    if pet_type == 'cat':
      pet_type = Cat
    elif pet_type == 'dog':
      pet_type = Dog
    else:
      return self.queue.dequeue()

    found_pet = None
    filter_queue = Queue()

    try:
      while True:
        current_pet = self.queue.dequeue()
        if isinstance(current_pet, pet_type) and not found_pet:
          found_pet = current_pet
        else:
          filter_queue.enqueue(current_pet)
    finally:
      self.queue = filter_queue
      return found_pet
