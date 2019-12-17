# Singly Linked List
The goal fo this code challenge is to make a simple linked list

### Links
[Tests](./test_linked_list.py)<br>
[Linked List Class](./linked_list.py)<br>
[Node Class](./node.py)<br>

## Challenge
Create 2 classes one for Nodes and one for Linked Lists. Create 3 functions to the linked list that 1:Adds a value to the front of the linked list, 2:Search throught the list to see if it contains the given value returning true or false, 3:Create a `__str__` function to print the list

## Approach & Efficiency
Insert: `O1`  <br>
Includes: `O(n)`<br>
To String: `O(n)`<br>

## APIs
Insert In: `value` -> Out: `None`  <br>
Includes In: `value` -> Out: `True/False`  <br>
To String In: `None` -> Out: `String`  <br>
# <br>
# Linked List Insertions
## Challenge
Create 3 methods for the linked list class all based around inserting the value in different locations. One for the end of the list. One for the before a given value and one for after a given value. Both the before and after should thow an error if the value you are looking for can not be found.

## Approach & Efficiency
Append: `O(n)`  <br>
Insert Before: `O(n)`  <br>
Insert After: `O(n)`  <br>

## APIs
Append: In: `Value` -> Out: `None`  <br>
Insert Before: In: `Search Term, Input Value` -> Out: `True/Error`  <br>
Insert After: In: `Search Term, Input Value` -> Out: `True/Error`  <br>

![](../../assets/Insert-Linked-List.jpg)

# <br>
# Kth Value From the End
## Challenge
Create a method that takes in an index and returns the value of the node at that position. If the position is outside of the bounds of the list the function should raise an error.

## Approach & Efficiency
#### kth_from_end:
* Time: `O(n)`<br>
* Space: `O`<br>

## APIs
kth_from_end: In: `Position` -> Out: `Value/Error`<br>


![](../../assets/Kth-From-End.png)

# <br>
# Merge Linked Lists
**I know that the instruction say to use a new file. I cleared this with JB so I could practice static methods**
## Challenge
Create a method that takes in 2 linked lists as the inputs and returns the head of the merged list as an output. The lists should be mreged in a zipper fasion (one then the other).

## Approach & Efficiency
#### mrege_linked_lists:
* Time: `O(n)`<br>
* Space: `O(1)`<br>

## APIs
merge_linked_lists: In: `ll_one, ll_two` -> Out: `merged_list_head`<br>


![](../../assets/Merge-Linked-List.jpg)
