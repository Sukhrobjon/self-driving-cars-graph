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

    print(f'{seperator}Chapter 2: Find your neighbors{seperator}')
    vertex_obj = graph.get_neighbors_of(to_vertex)
    print(f"{vertex_obj}")

    print(f'{seperator}Chapter 3: N level connections{seperator}')
    print(graph.n_level_bfs(from_vertex, 1))

    print(f'{seperator}Chapter 4: Finding the Path{seperator}')
    path = (graph.dfs_paths(from_vertex, to_vertex, set()))
    print(path[::-1])

    print(f"{seperator}Chapter 5: Shortest Path{seperator}")
    shortest_path = graph.find_shortest_path(from_vertex, to_vertex)
    print(f"Verticies in shortest path: {shortest_path[0]}")
    print(f"Number of edges in shortest path: {shortest_path[1]}")

    print(f"{seperator}Chapter 6: Clique Discovery{seperator}")
    clique = graph.clique()
    print(f"The clique in this graph {clique}")

if __name__ == "__main__":

    filename = sys.argv[1]
    main(filename)
