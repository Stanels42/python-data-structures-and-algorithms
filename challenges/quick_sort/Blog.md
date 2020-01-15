### [Read Me](./README.md)

## The How of Quick Sort
The short version of what quick sort does is it takes a list decides on a pivot and places all values greater then the pivot on one side and all less then on the other. This will make sure that the pivot that the program decided on is in it's sorted position.<br>
This process is repeated again treating the left and right sections as their own lists and selecting a new pivot.

<pre>
In:
[7,6,5,2,9,4,8,0,1,3]

Pivot = 3
[1,0,2][3][7,6,5,9,4,8]
3 is sorted

[1,0,2]
Pivot = 2
[1,0][2]
2 is sorted

[1,0]
Pivot = 0
[0][1]
All sorted

[7,6,5,9,4,8]
Pivot = 8
[7,6,5,4][8][9]
8 is sorted

[7,6,5,4]
Pivot = 4
[4][7,6,5]
4 is sorted

[7,6,5]
Pivot = 5
[5][7,6]
5 is sorted

[7,6]
Pivot = 6
[6][7]
6 is sorted

[0][1][2][3][4][5][6][7][8][9]
All Sorted

Out:
[0,1,2,3,4,5,6,7,8,9]
</pre>
