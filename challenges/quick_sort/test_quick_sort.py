######################
## Import Libraries ##
######################

import pytest

##################
## Import Files ##
##################

from quick_sort import quick_sort, shuffle

####################
## Pytest Fixture ##
####################

@pytest.fixture()
def lst():
  arr = []
  for i in range(300):
    arr.append(i)
  return arr

##################
## Test Shuffle ##
##################

def test_shuffle():
  lst = [0,1,2,3,4,5,6,7,8,9]
  new_lst = shuffle(lst)
  assert lst != new_lst

def test_sort_short_list():
  lst = [0,1,2,3,4,5,6,7,8,9]
  new_lst = shuffle(lst)
  quick_sort(new_lst)
  assert lst == new_lst

def test_sort_long_list(lst):
  new_lst = shuffle(lst)
  quick_sort(new_lst)
  assert lst == new_lst

def test_reverse(lst):
  new_lst = lst[::-1]
  quick_sort(new_lst)
  assert lst == new_lst

def test_almost_sorted():
  lst = [0,1,2,3,4,5,6,7,8,9]
  new_lst = [9,1,2,3,4,5,6,8,7,0]
  quick_sort(new_lst)
  assert lst == new_lst

def test_letters():
  lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  new_lst = shuffle(lst)
  quick_sort(new_lst)
  assert lst == new_lst
