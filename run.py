import sys
from Graphs.graph import Graph, Vertex, build_graph
from Graphs.read_file import read_file


def main(filename):

    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)

    seperator = "========================="

    from_vertex = "1"
    to_vertex = "4"
    # grab the edges and vertices from graph object
    g_edges = graph.edge_list
    g_vertices = graph.get_vertices()

    print(f'{seperator}Chapter 1: Make a graph{seperator}')
    print(f'Vertices: {g_vertices}')
    print(f'Number of Edges: {len(g_edges)}')
    print("The Edge List:")
    for edge in g_edges:
        print(edge)

if __name__ == "__main__":

    filename = sys.argv[1]
    main(filename)