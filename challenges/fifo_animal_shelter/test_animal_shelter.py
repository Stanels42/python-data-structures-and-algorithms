import pytest

####################
## Import Classes ##
####################

from fifo_animal_shelter import Animal_Shelter, EmptyListError, NonShelterAnimal
from pet import Pet, Cat, Dog, Fish

####################
## Test Existence ##
####################

def test_shelter():
  assert Animal_Shelter()

def test_cat():
  assert Dog('Dogbert')

def test_dog():
  assert Cat('Dr. Funyuns')

##############
## Fixtures ##
##############

@pytest.fixture()
def shelter():
  return Animal_Shelter()

#####################################
## Test Adding And Removing Values ##
#####################################

def test_add_remove_one_dog(shelter):
  shelter.enqueue(Dog('bax'))
  shelter.enqueue(Cat('cocoa'))
  assert shelter.dequeue('dog').name == 'bax'

def test_add_remove_one_cat(shelter):
  shelter.enqueue(Dog('bax'))
  shelter.enqueue(Cat('cocoa'))
  assert shelter.dequeue('cat').name == 'cocoa'

def test_add_remove_multi_cat(shelter):
  shelter.enqueue(Cat('penguin'))
  shelter.enqueue(Cat('cocoa'))
  assert shelter.dequeue('cat').name == 'penguin'
  assert shelter.dequeue('cat').name == 'cocoa'

def test_add_non_valid_pet(shelter):
  with pytest.raises(NonShelterAnimal):
    shelter.enqueue(Fish('Bubbles'))

def test_remove_from_empty(shelter):
  with pytest.raises(EmptyListError):
    shelter.dequeue('cat')

def test_remove_non_valid_pet(shelter):
  assert shelter.dequeue('fish') == None
