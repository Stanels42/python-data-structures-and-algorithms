### [Read Me](./README.md)
# Insertion Sort
### Input: [5,3,4,1,2]
#### Step One:
List = [`5`,3,4,1,2]<br>
Current = 5<br>

#### Step Two:
List = [`3`,5,4,1,2]<br>
Current = 3<br>


#### Step Three:
List = [3,`4`,5,1,2]<br>
Current = 4<br>

#### Step Three:
List = [`1`,3,4,5,2]<br>
Current = 1<br>

#### Step Four:
#### Full
List = [1,3,4,5,`2`]<br>
Current = 2<br>
2 < 5 <br>
List = [1,3,4,`2`,5]<br>
2 < 4<br>
List = [1,3,`2`,4,5]<br>
2 < 3<br>
List = [1,`2`,3,4,5]<br>
2 > 1<br>
List = [1,`2`,3,4,5]<br>
\> Inserted <
### Output: [1,2,3,4,5]
