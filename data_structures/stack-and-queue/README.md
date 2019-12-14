# Stacks and Queues
The goal fo this code challenge is to make a simple linked list

### Links
[Node Class](./node.py)<br>
<br>
[Stack Class](./stack.py)<br>
[Stack Tests](./test_stack.py)<br>
<br>
[Queue Class](./queue.py)<br>
[Queue Tests](./test_queue.py)<br>

## Challenge
Create 2 classes one for Nodes and one for Linked Lists. Create 3 functions to the linked list that 1:Adds a value to the front of the linked list, 2:Search throught the list to see if it contains the given value returning true or false, 3:Create a `__str__` function to print the list

## Approach & Efficiency
#### Stacks
Enque: `O(1)`<br>
Deque: `O(1)`<br>
Peek: `O(1)`<br>
Is Empty: `O(1)`<br>
#### Queues
Enque: `O(1)` or `O(n)` if used with existing list<br>
Deque: `O(1)`<br>
Peek: `O(1)`<br>
Is Empty: `O(1)`<br>

## APIs
Enque In: `value` -> Out: `None`  <br>
Deque In: `None` -> Out: `Removed Node`  <br>
Peek In: `None` -> Out: `First Value`  <br>
Is Empty In: `None` -> Out: `True/False`  <br>
