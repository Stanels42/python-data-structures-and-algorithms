[Home](../../README.md)
# Graphs

[Code](./graphs.py)<br>
[Tests](./test_graphs.py)

## Challenge/Data Structure
Today's data structure is to create a graph. The corresponding methods in the graph that we need to flesh out are `add`, `add_edge`, `get_neighbors`, `get_vertices` and `size`
## Approach
`add`
  - Takes in a value and creates a vertex. The new vertex is added to the the graph. Finally return the new vertex.<br>

`add_edge`
  - Takes in 2 vertices that are in the graph. There is an optional parameter for weight. <br>

`get_neighbors`
  - Takes in a vertex and returns all other vertices that it has connections to.<br>

`get_vertices`
  - Returns a list of all vertices that are in the graph.<br>

`size`
  - There us an internal dictionary that is used by the graph. returning the size will tell you the number of<br>
## API
`add`
  - In: Value
  - Out: Vertex with the value

`add_edge`
  - In: 2 vertices, optional: Weight `<int>`
  - Out: None

`get_neighbors`
  - In: Vertex
  - Out: List of tuples containing edges `(<vertex>, Weight)`

`get_vertices`
  - In: `None`
  - Out: List of all `<vertices>`

`size`
  - In: None
  - Out: Number of vertices (`<int>`)
