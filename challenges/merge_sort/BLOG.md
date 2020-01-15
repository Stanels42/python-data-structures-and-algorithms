<pre>
[5,1,3,2,4] # Input
  /      \
[5,1,3]  [2,4] # Split the list into sub lists based on the mid
  /   \    \  \
[5,1] [3]  [2] [4]
 / \     \    \   \
[5] [1]  [3]  [2] [4] # Separate the list to the smallest parts
 \   /   /    /   /
[1,5]  [3]  [2] [4] # Sort the value as you merge the lists back together
   |   /    /  /
[1,3,5]   [2,4]
    \     /
[1,2,3,4,5] # Output
</pre>
