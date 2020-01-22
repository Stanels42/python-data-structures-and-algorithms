[Home](../../README.md)
# Find Common Tree Values
## Challenge
The Goal of this challenge is to create a function that takes in 2 binary trees as an input. It will the return a set of all values that they have in common.

- [Code](./common_tree.py)
- [Tests](./test_common_tree.py)
- [Tree](./tree.py)

## Approach
There are 3 helper functions that make up my approach to this problem.
1) First is the `recurse` function. This takes in a node and recursively travels over the remainder of a tree. The important part is it also takes an action function. THe action is preformed on the current node.
<br>Recurse the first Tree
2) `Tree one action`. This one is really simple and populates a set with all unique values with in the Tree it's self.
<br>Recurse the second Tree
3) `Tree two action` This is where the trees are compared. If the value of the current node is in the set from the previous tree the value is added to the output set.<br>

At the end the output set is returned.
## API
`find_common(tree1, tree2)`
- In: 2 Binary Trees
- Out: Set of common values
## Efficiency
`find_common()`
- Time: `O(n)`
- Space: `O(n)`

### Image
![Missing Image](../../assets/Find_Common_Tree_Values.jpg)
