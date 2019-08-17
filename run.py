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

    print(f'{seperator}Problem One: Fastest Route{seperator}')
    fastest_route = graph.find_fastest_route(from_vertex, to_vertex)

    if fastest_route:
        print(f"Fastest route from {from_vertex} to {to_vertex} is: ", end="")
        print(*fastest_route[0], sep="->", end=" ")
        print(f"with total distance of {fastest_route[1]} miles!")
    else:
        print(f"We couldn't find route from {from_vertex} to {to_vertex}")

    print(f"{seperator}Problem Two: Busiest Intersection{seperator}")
    busy_intersection = graph.busiest_intersection()
    # print(f"Busy intersection(s) {busy_intersection[0]}")
    print(*busy_intersection[0], sep=", ", end="")
    print(f" connected {busy_intersection[1]} of intersections.")

    print(f"{seperator}Problem Three: Find near me{seperator}")
    n_miles = 25
    near_locations = graph.find_near_me(from_vertex, n_miles)
    print(f"These locations are {n_miles} away from {from_vertex}.")
    print("Locations are:", end=" ")
    print(*near_locations, sep=", ")

if __name__ == "__main__":

    filename = sys.argv[1]
    main(filename)
