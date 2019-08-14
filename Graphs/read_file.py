
from Graphs.graph import Graph, Vertex

def read_file(filename):
    """Read the txt file containg graph information and return them
    in a list

    Args: 
        filename (txt): takes a text file to read from

    Returns:
        graph elements (tuple): Tuple of graph object, list of vertices and edges
    """
    edges = []
    with open(filename, 'r') as file:
        for counter, line in enumerate(file):
            
            # get type of the graph
            if counter == 0:
                graph_type = line.strip()
                # create undirected graph
                if graph_type == 'G':
                    graph = Graph(directed=False)
                elif graph_type == 'D':
                    graph = Graph(directed=True)
                else:
                    raise ValueError("Graph type is not specified correctly, type can be 'G' or 'D'!")

            # get vertices
            elif counter == 1:
                vertices = line.strip().split(',')

            # grab all the edges
            else:

                edge = line.strip('()\n').split(',')
                if len(edge) > 3 or len(edge) < 2:
                    raise Exception("Edges must contain 2 or 3 values!")
                edges.append(edge)

    return graph, vertices, edges



