#!python
from queue import Queue, PriorityQueue


class Vertex(object):
    """ Vertex Class:
    A helper class for the Graph class that defines vertices and vertex
    neighbors.
    """
    def __init__(self, data):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.data = data
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""

        self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.data} adjacent to {[x.data for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this(self) vertex."""
        return self.neighbors.keys()

    def get_id(self):
        """Return the data of this vertex."""
        return self.data

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # vertex to the given vertex.
        return self.neighbors[vertex] if vertex in self.neighbors else None


class Graph:
    """ Graph Class A class demonstrating the essential
        facts and functionalities of graphs.
    """
    def __init__(self, directed=False):
        """Initialize a graph object with an empty dictionary."""
        self.vert_dict = {}
        # unique edge_list
        self.edge_list = []
        self.num_vertices = 0
        self.num_edges = 0
        self.DEFAULT_WEIGHT = 0
        self.directed = directed

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax:
        for v in g"""
        return iter(self.vert_dict.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return
        the vertex.

        Args:
            key(str): a new vertex to be added

        Returns:
            new key(Vertex): returns vertex object containing new vertex
        """

        if key in self.vert_dict:
            print(f'Vertex {key} already exists')
            return

        # create a new vertex
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex
        self.num_vertices += 1

        return new_vertex

    def get_vertex(self, key):
        """Obtains the key(vertex) from graph

        Args:
            key(str): a new vertex to be added

        Returns:
            vertex(Vertex): asked vertex object none if not found
        """
        if key in self.vert_dict.keys():
            return key
        return None

    def get_neighbors_of(self, vertex):
        """Grabs all the neighbors of the current vertex

        Args:
            vertex (str): a given vertex

        Returns:
            vertex (Vertex): Vertex object if found
        """
        if vertex in self.vert_dict:
            return self.vert_dict[vertex]

        raise KeyError("The vertex not found in the Graph!")

    def add_edge(self, from_vertex, to_vertex, weight=None):
        """Add the edge: Connects the two vertices with associated weight

        Args:
            from_vertex(str): start vertex(first vertex to be connected)
            to_vertex(str): end vertex(second vertex to be connected)
            weight(int): weight associated with two vertices, 0 by default
        """

        if from_vertex == to_vertex:
            print(f'You cant add the vertex to itself!')
            return

        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise ValueError("One of the vertex doesn't exist!")

        # assigning the weight
        if weight is None:
            weight = self.DEFAULT_WEIGHT
        else:
            weight = int(weight)

        edge = (from_vertex, to_vertex, weight)
        # handling duplicated edges in input file
        if edge in self.get_edges():
            raise ValueError("You can't add duplicated edges!")

        from_vert_obj = self.vert_dict[from_vertex]
        to_vert_obj = self.vert_dict[to_vertex]

        if self.directed:  # directed graph
            from_vert_obj.add_neighbor(to_vert_obj, weight)
        else:
            # connect the edges in both ways
            from_vert_obj.add_neighbor(to_vert_obj, weight)
            to_vert_obj.add_neighbor(from_vert_obj, weight)

        # add edges to unique edge_list
        self.edge_list.append(edge)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return list(self.vert_dict.keys())

    def get_edges(self):
        """Return number of all edges in the graph"""
        edges = []
        for v in self.vert_dict.values():
            for w in v.neighbors:
                edges.append((v.data, w.data, v.get_edge_weight(w)))
        return edges

    def find_fastest_route(self, from_vertex, to_vertex):
        """Finds for the shortest path from vertex a to b using
        Dijkstra's algorithm:
        https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

        Args:
            from_vertex (str) : Starting point on the graph
            to_vertex (str) : The final distanation

        Returns:
            shortest path (tuple): List of vertices in the path and len
                                    Empty list if path does not exist
        """

        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise KeyError("Either or both of the keys are not in the graph!")

        starting_vert = self.vert_dict[from_vertex]

        # Vertex is to itself, no edges which means no weight!
        if from_vertex == to_vertex:
            return [starting_vert], 0

        # Initialize our priority queue and path
        queue = PriorityQueue()
        queue.put(PriorityEntry(0, starting_vert))
        path = {starting_vert.data: (0, None)}

        # Iterate through all the verts and enqueue them
        for vert_key, vert in self.vert_dict.items():
            if vert_key != starting_vert.data:
                path[vert_key] = (float("inf"), None)
                queue.put(PriorityEntry(float("inf"), vert))

        # While the queue isn't empty
        while not queue.empty():

            # Grab the piece of data from the queue and get it's current weight
            curr_vert = queue.get().data
            curr_vert_weight, _ = path[curr_vert.data]
            # Iterate through the neighbors of the current vertex
            for neighbor, weight in curr_vert.neighbors.items():

                # Get the neighbors weight
                prev_neighbor_weight, _ = path[neighbor.data]
                total_weight = weight + curr_vert_weight

                # Check if the new total weight is greater than what the
                # neighbors previous weight is
                if total_weight < prev_neighbor_weight:
                    path[neighbor.data] = (total_weight, curr_vert)
                    queue.put(PriorityEntry(total_weight, neighbor))

        # No path was found to the vertex, infinite weight away.
        overall_weight, prev = path[to_vertex]
        if overall_weight == float("inf"):
            return [], overall_weight

        # Recreate the path
        goal = self.vert_dict[to_vertex]
        minimal_path = [goal]

        while prev:
            minimal_path.append(prev)
            _, prev = path[prev.data]

        # grab only vertex data to make it easy to visualize
        minimal_path = [node.data for node in minimal_path]

        return minimal_path[::-1], overall_weight

    def busiest_intersection(self):
        """Find the busiest intersection by determining the most connected
        vertex.

        Returns:
            busy_vertex(str): The most connected vertex
        """
        # store the num of neighbors to compare later
        num_neighbor = []
        for vertex in self.vert_dict:
            curr_vert = self.vert_dict[vertex]
            num_neighbor.append(len(curr_vert.neighbors))

        # get the max num of vertex
        max_neighbor = max(num_neighbor)

        # finding the all busiest intersection
        busy_intersections = []
        for vertex in self.vert_dict:
            curr_vert = self.vert_dict[vertex]
            if len(curr_vert.neighbors) == max_neighbor:
                busy_intersections.append(curr_vert.data)

        return busy_intersections, max_neighbor

    def find_near_me(self, from_vertex, n_miles):
        """Find the all vertices(locations) n_miles away from the starting
        vertex

        Args:
            from_vertex(str): starting point
            n_miles(int): n_miles away from starting point

        Returns:
            locations(list): list of all vertices at least n_miles away
            from starting point
        """
        near_locations = []

        for vertex in self.vert_dict:
            curr_vert = self.vert_dict[vertex]
            if curr_vert.data != from_vertex:
                # get the fastest way to each locations
                dist = self.find_fastest_route(from_vertex, curr_vert.data)
                if dist[1] <= n_miles:
                    # add to near locations if the distance is less than the
                    # specified n_miles away
                    near_locations.append(curr_vert.data)
        return near_locations


def build_graph(graph: Graph, vertices, edges):
    """Creates a graph with vertices and edges

    Args:
        graph(Graph): Graph object
        vertices(list): list of vertices passed to build graph
        edges(list): list of edges passed to build graph

    Returns:
        graph(Graph): Graph object with its edges and vertices added
    """
    # add the vertices
    for vertex in vertices:
        graph.add_vertex(vertex)

    # add the edges
    for edge in edges:
        # unpack the edge, because it could be len of 2 or 3
        graph.add_edge(*edge)

    return graph


class PriorityEntry(object):
    """This is helper class for Priority Queue
    Source: https://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts

    As there is no priority queue enqueue method implementation
    this class serves as wraper for that. It add the min weighted edges
    at the 0th index in the queue
    """

    def __init__(self, priority, data):
        """Initialize Priority entry object"""
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        """The function orders two instances of the class by their priorities only,
        and not by their data
        """
        return self.priority < other.priority
