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
  for i in range(300):
    lst.append(i)
  return lst

@pytest.fixture()
def mixed_arr():
  lst = []
  for i in range(300):
    lst.append(i)
  return shuffle(lst)

@pytest.fixture()
def reverse_lst():
  lst = []
  for i in range(300):
    lst.append(299 - i)
  return lst

##################
## Test Shuffle ##
##################

def test_shuffle():
  arr = [0,1,2,3,4,5,6,7,8,9]
  new_arr = shuffle(arr)
  assert arr != new_arr

def test_sort_short_list():
  arr = [1,2,3,4,5]
  scrambled_lst = [2,1,5,3,4]
  insertion_sort(scrambled_lst)
  assert arr == scrambled_lst

def test_sort_long_list(arr, mixed_arr):
  insertion_sort(mixed_arr)
  assert mixed_arr == arr

def test_reverse_list(arr, reverse_lst):
  insertion_sort(reverse_lst)
  assert reverse_lst == arr

def test_letters():
  lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  new_lst = shuffle(lst)
  assert lst != new_lst
  insertion_sort(new_lst)
  assert lst == new_lst
