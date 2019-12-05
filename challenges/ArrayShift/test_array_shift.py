import pytest

from array_shift import insert_shift_array, remove_center

################
# Insert Shift #
################

# Test Even List
def test_one():
  actual = insert_shift_array([1,2,4,5], 3)
  expected = [1,2,3,4,5]
  assert actual == expected

# Test Odd List
def test_two():
  actual = insert_shift_array([1,2,4], 3)
  expected = [1,2,3,4]
  assert actual == expected

# Test Different Data Types
def test_three():
  actual = insert_shift_array(['a','b','c','d'], 'x')
  expected = ['a','b','x','c','d']
  assert actual == expected

# Test Empty List
def test_four():
  actual = insert_shift_array([], 'a')
  expected = ['a']
  assert actual == expected

# Test Non Data Type
def test_five():
  actual = insert_shift_array([], None)
  expected = [None]
  assert actual == expected

# String Type Error
def test_six():
  with pytest.raises(TypeError):  # Pass in the expected error
    result = insert_shift_array('String', 'x')

#################
# Remove Center #
#################

# Odd Length
def test_one_remove():
  actual = remove_center([1,2,3,4,5,6,7])
  expected = [1,2,3,5,6,7]
  assert actual == expected

# Even Length
def test_two_remove():
  actual = remove_center([1,2,3,4,5,6])
  expected = [1,2,3,5,6]
  assert actual == expected

# Different Data Types
def test_three_remove():
  actual = remove_center(['a',2,'c','x','d',6,'e'])
  expected = ['a',2,'c','d',6,'e']
  assert actual == expected

# Empty List
def test_four_remove():
  actual = remove_center([])
  expected = []
  assert actual == expected

# Trying a String
def test_five_remove():
  actual = remove_center('String')
  expected = 'Strng'
  assert actual == expected
