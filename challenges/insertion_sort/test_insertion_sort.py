######################
## Import Libraries ##
######################

import pytest

#####################
## Import Function ##
#####################

from insertion_sort import insertion_sort, shuffle

#####################
## Pytest Fixtures ##
#####################

@pytest.fixture()
def arr():
  lst = []
  for i in range(21):
    lst.append(i)
  return lst

@pytest.fixture()
def mixed_arr():
  lst = []
  for i in range(21):
    lst.append(i)
  lst = shuffle(lst)
  return lst

##################
## Test Shuffle ##
##################

def test_shuffle():
  arr = [1,2,3,4,5]
  new_arr = shuffle(arr)
  assert arr != new_arr

def test_array_sort(arr, mixed_arr):
  insertion_sort(mixed_arr)
  assert mixed_arr == arr
