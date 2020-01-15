######################
## Import Libraries ##
######################

import pytest

##################
## Import Files ##
##################

from merge_sort import merge_sort, shuffle

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
  new_lst = merge_sort(new_lst)
  assert lst == new_lst

def test_sort_long_list():
  lst = []
  for i in range(300):
    lst.append(i)
  new_lst = shuffle(lst)
  new_lst = merge_sort(new_lst)
  assert lst == new_lst

def test_reverse():
  lst = []
  for i in range(300):
    lst.append(300-i)
  new_lst = shuffle(lst)
  new_lst = merge_sort(new_lst)
  assert lst[::-1] == new_lst

def test_almost_sorted():
  lst = [0,1,2,3,4,5,6,7,8,9]
  new_lst = [0,1,2,3,4,5,6,8,7,9]
  new_lst = merge_sort(new_lst)
  assert lst == new_lst
