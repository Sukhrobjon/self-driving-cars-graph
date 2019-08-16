import sys
from Graphs.graph import Graph, Vertex, build_graph
from Graphs.read_file import read_file


def main(filename):

    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)

    seperator = "========================="

    from_vertex = "A"
    to_vertex = "C"
    # grab the edges and vertices from graph object
    g_edges = graph.edge_list
    g_vertices = graph.get_vertices()

    print(f'{seperator}Visualize the map: Make a graph{seperator}')
    print(f'Vertices: {g_vertices}')
    print(f'Number of Edges: {len(g_edges)}')
    print("The Edge List:")
    for edge in g_edges:
        print(edge)

    print(f'{seperator}Problem One{seperator}')
    print(f"Dijkstras path {graph.find_fastest_route(from_vertex, to_vertex)}")


if __name__ == "__main__":

    filename = sys.argv[1]
    main(filename)
