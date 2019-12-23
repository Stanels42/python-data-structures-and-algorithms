### [Home](../../README.md)

# Fizz Buzz Tree
Create a function called fizz_buzz_tree that takes in a tree of nodes with int values then will return a new tree that has replaced `%3`, `%5` and `%15` values with `Fizz`, `Buzz` and `FizzBuzz` respectivly.

## Challenge
Make a function that takes in a binary tree of ints as a parameter and returns a tree of strings that has replaced the values based on FizzBuzz principles. If the given node is not evenly divisible by 3 or 5 just make the value into a string and then add it to the tree. <br>
I used 2 helper functions in my code one that handles recursive calls and another to handle the selection of Fizz or Buzz. Also if the inital tree is empty I just return an empty tree.

## Approach & Efficiency
Functions:
fizz_buzz_tree: _time:_ `O(n)` _space:_ `O(h+n)`<br>
For the space I believe the max memory usage is the number of nodes that are in the new tree + the height of the old tree that makes up the recursive stack.

## Solution
#### [Code](./fizz_buzz_tree.py)<br>
#### [Tests](./test_fizz_buzz_tree.py)<br>
#### Other Helper Files
* [Tree](./tree.py)
* [Queue](./queue.py)
* [Node](./node.py)

__I opted to compleate the assignment solo and in the process didn't have a whiteboard__
