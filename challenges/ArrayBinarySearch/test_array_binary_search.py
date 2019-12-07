import pytest
from array_binary_search import binary_search

def test_example_one():
  expected = 2
  actual = binary_search([4,8,15,16,23,42], 15)
  assert actual == expected

def test_example_two():
  expected = -1
  actual = binary_search([11,22,33,44,55,66,77], 90)
  assert actual == expected

def test_strings():
  expected = 2
  actual = binary_search(['a','b','c','d','e','f'], 'c')
  assert expected == actual

# def test_string_typeError():
#   with pytest.raises(TypeError):  # Pass in the expected error
#     result = insert_shift_array('String', 'r')
