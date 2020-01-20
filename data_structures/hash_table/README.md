[Home](../../README.md)

# Hash Table


### Links
[Hash Table](./hash_table.py)<br>
[Hash Table Tests](./test_hash_table.py)<br>

## Challenge
The code challenge was to create a hash table. The approach I used was to create a list of linked lists. You have the option to set the length of the base list in the init function (default: 1024). The spaces are set to None until a value is inserted at that point. At that point a linked list is created at that index. The linked lists have the same functionality as the hash table of add contains and get.

## Approach & Efficiency
Add:<br>
  - Time: `O(1)`<br>
  - Space: `O(1)`<br>

Contains:
  - Time: `O(1)`<br>
  - Space: `O(1)`<br>

Get:<br>
  - Time: `O(1)`<br>
  - Space: `O(1)`<br>

Hash:<br>
  - Time: `O(1)`<br>
  - Space: `O(1)`<br>

## API
Add:
  - In: `(Key, Value)`
  - Out: `None`

Contains:
  - In:`Key`
  - Out:`True/False`

Get:
  - In: `Key`
  - Out: `Value`

Hash:
  - In: `Key` Int or String
  - Out: `Index` Int of position in List
