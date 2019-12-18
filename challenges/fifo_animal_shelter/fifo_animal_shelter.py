from pet import Cat, Dog
from queue import Queue, EmptyListError

class Animal_Shelter:
  def __init__(self):
    """"Create a queue for cats na done for dogs"""
    self.dog_queue = Queue()
    self.cat_queue = Queue()

  def enqueue(self, pet):
    """Take in a Cat or Dog object and adds it to their respective list. If not one of those animals raise an error"""
    if isinstance(pet, Dog):
      self.dog_queue.enqueue(pet)
    elif  isinstance(pet, Cat):
      self.cat_queue.enqueue(pet)
    else:
      raise NonShelterAnimal

  def dequeue(self, pet = None):
    """Given a string as input will remove a cat or dog from it's respective list. If not a Cat or Dor return `None`"""
    if pet.lower() == 'dog':
      return self.dog_queue.dequeue()
    elif pet.lower() == 'cat':
      return self.cat_queue.dequeue()
    return None

class NonShelterAnimal(ValueError):
  """If the animal you are trying to access is not one the shelter keeps"""
  pass
