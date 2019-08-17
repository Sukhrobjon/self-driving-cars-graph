# Graphs.graph

## Vertex
```python
Vertex(self, data)
```
Vertex Class:
A helper class for the Graph class that defines vertices and vertex
neighbors.

### add_neighbor
```python
Vertex.add_neighbor(self, vertex, weight=0)
```
Add a neighbor along a weighted edge.
### get_neighbors
```python
Vertex.get_neighbors(self)
```
Return the neighbors of this(self) vertex.
### get_id
```python
Vertex.get_id(self)
```
Return the data of this vertex.
### get_edge_weight
```python
Vertex.get_edge_weight(self, vertex)
```
Return the weight of this edge.
## Graph
```python
Graph(self, directed=False)
```
Graph Class A class demonstrating the essential
facts and functionalities of graphs.

### add_vertex
```python
Graph.add_vertex(self, key)
```
Add a new vertex object to the graph with the given key and return
the vertex.

Args:
    key(str): a new vertex to be added

Returns:
    new key(Vertex): returns vertex object containing new vertex

### get_vertex
```python
Graph.get_vertex(self, key)
```
Obtains the key(vertex) from graph

Args:
    key(str): a new vertex to be added

Returns:
    vertex(Vertex): asked vertex object none if not found

### get_neighbors_of
```python
Graph.get_neighbors_of(self, vertex)
```
Grabs all the neighbors of the current vertex

Args:
    vertex (str): a given vertex

Returns:
    vertex (Vertex): Vertex object if found

### add_edge
```python
Graph.add_edge(self, from_vertex, to_vertex, weight=None)
```
Add the edge: Connects the two vertices with associated weight

Args:
    from_vertex(str): start vertex(first vertex to be connected)
    to_vertex(str): end vertex(second vertex to be connected)
    weight(int): weight associated with two vertices, 0 by default

### get_vertices
```python
Graph.get_vertices(self)
```
Return all the vertices in the graph
### get_edges
```python
Graph.get_edges(self)
```
Return number of all edges in the graph
### find_fastest_route
```python
Graph.find_fastest_route(self, from_vertex, to_vertex)
```
Finds for the shortest path from vertex a to b using
Dijkstra's algorithm:
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Args:
    from_vertex (str) : Starting point on the graph
    to_vertex (str) : The final distanation

Returns:
    shortest path (tuple): List of vertices in the path and len
                            Empty list if path does not exist

### busiest_intersection
```python
Graph.busiest_intersection(self)
```
Find the busiest intersection by determining the most connected
vertex.

Returns:
    busy_vertex(str): The most connected vertex

### find_near_me
```python
Graph.find_near_me(self, from_vertex, n_miles)
```
Find the all vertices(locations) n_miles away from the starting
vertex

Args:
    from_vertex(str): starting point
    n_miles(int): n_miles away from starting point

Returns:
    locations(list): list of all vertices at least n_miles away
    from starting point

## build_graph
```python
build_graph(graph: Graphs.graph.Graph, vertices, edges)
```
Creates a graph with vertices and edges

Args:
    graph(Graph): Graph object
    vertices(list): list of vertices passed to build graph
    edges(list): list of edges passed to build graph

Returns:
    graph(Graph): Graph object with its edges and vertices added

## PriorityEntry
```python
PriorityEntry(self, priority, data)
```
This is helper class for Priority Queue
Source: https://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts

As there is no priority queue enqueue method implementation
this class serves as wraper for that. It add the min weighted edges
at the 0th index in the queue

