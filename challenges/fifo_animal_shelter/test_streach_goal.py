import pytest

####################
## Import Classes ##
####################

from streach_goal import AnimalShelter, EmptyListError
from pet import Pet, Cat, Dog, Fish

####################
## Test Existence ##
####################

def test_shelter():
  assert AnimalShelter()

def test_cat():
  assert Dog('Dogbert')

def test_dog():
  assert Cat('Dr. Funyuns')

##############
## Fixtures ##
##############

@pytest.fixture()
def shelter():
  return AnimalShelter()

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


def test_add_dequeue(shelter):
  shelter.enqueue(Dog('bax'))
  shelter.enqueue(Dog('boomer'))
  shelter.enqueue(Dog('echo'))
  shelter.enqueue(Cat('cocoa'))
  assert shelter.dequeue('dog').name == 'bax'
  assert shelter.dequeue('cat').name == 'cocoa'


def test_add_remove_multi_cat(shelter):
  shelter.enqueue(Cat('penguin'))
  shelter.enqueue(Dog('echo'))
  shelter.enqueue(Cat('cocoa'))
  assert shelter.dequeue('cat').name == 'penguin'
  assert shelter.dequeue('cat').name == 'cocoa'

def test_remove_from_empty(shelter):
  assert None == shelter.dequeue('cat')

