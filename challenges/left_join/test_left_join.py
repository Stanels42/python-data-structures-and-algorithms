######################
## Import Libraries ##
######################

import pytest

##################################
## Import Functions and Helpers ##
##################################

from helper_hash_table import HashTable
from left_join import join

##################
## Test Imports ##
##################

def test_imports():
  assert join
  assert HashTable

#####################
## Test Hash Table ##
#####################

def test_add():
  HT = HashTable()
  HT.add('key','value1')
  HT.add('key', 'value2')
  assert HT['key']
  assert HT.get('key') == 'value2'

def test_dunder_methods():
  HT = HashTable()
  HT['key1'] = 'value1'
  HT['key2'] = 'value2'
  assert 'key1' in HT
  assert HT['key2'] == 'value2'

##########################
## Fixtures and Helpers ##
##########################

def make_table(count=10, offset=0, step=1):
  HT = HashTable()
  for index in range(count):
    key = f'key {(index * step) + offset}'
    HT.add(key, f'{index} value')
  return HT

###########
## Tests ##
###########

@pytest.mark.parametrize(
  "left, right, expected",
    [
      ({'fond':'enamored','wrath':'anger','outfit': 'grab','flow': 'direction',},{'fond': 'averse','wrath': 'delight','flow': 'jam',},('fond', 'enamored','averse')),
      (make_table(), make_table(), ('key 1', '1 value', '1 value')),
      (make_table(), make_table(offset=2), ('key 8', '8 value', '6 value')),
      (make_table(count=2), make_table(count=2, offset=10), ('key 0', '0 value', None)),
    ]
)
def test_left_join(left, right, expected):
  actual = join(left, right)
  assert expected in actual



@pytest.mark.parametrize(
  "left, right, expected",
    [
      ({'fond':'enamored','wrath':'anger','outfit': 'grab','flow': 'direction',},{'fond': 'averse','wrath': 'delight','flow': 'jam',},('fond', 'enamored','averse')),
      (make_table(), make_table(), ('key 1', '1 value', '1 value')),
      (make_table(), make_table(offset=2), ('key 8', '8 value', '6 value')),
      (make_table(count=2), make_table(count=2, offset=10), ('key 0', '0 value', None)),
    ]
)
def test_right_join(left, right, expected):
  # Swap so 'left' becomes 'right' and 'right' becomes 'left' then left join
  actual = join(right, left, join_right=True)
  assert expected in actual
