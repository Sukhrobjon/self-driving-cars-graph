#!python

from Graphs.graph import Vertex, Graph
import unittest


class VertexTest(unittest.TestCase):

    def test_init(self):
        vertex_1 = Vertex('A')
        assert vertex_1.get_id() is 'A'
        assert vertex_1.neighbors == {}

    def test_add_neighbor(self):
        vertex_1 = Vertex('A')
        # add a neighbor without weight
        vertex_2 = 'B'
        vertex_1.add_neighbor(vertex_2)
        assert vertex_2 in vertex_1.neighbors
        assert len(vertex_1.get_neighbors()) is 1
        assert vertex_1.get_edge_weight(vertex_2) is 0

        # add another vertex with weight
        vertex_3 = 'C'
        vertex_1.add_neighbor(vertex_3, 5)
        assert vertex_3 in vertex_1.neighbors
        assert len(vertex_1.get_neighbors()) is 2
        assert vertex_1.get_edge_weight(vertex_3) is 5

        # adding duplicate neighbor
        vertex_1.add_neighbor(vertex_2, 3)
        assert vertex_2 in vertex_1.neighbors
        assert len(vertex_1.get_neighbors()) is 2
        assert vertex_1.get_edge_weight(vertex_2) is 3


class GraphTest(unittest.TestCase):

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")

        self.assertEqual(2, len(graph.get_vertices()))
        self.assertIsInstance(graph.get_vertex('A'), Vertex)

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")

        graph.add_edge("A", "C")
        graph.add_edge("A", "C", 3)

        self.assertEqual(3, len(graph.get_vertices()))
        self.assertEqual(2, len(graph.edge_list))
        graph.add_vertex("E")
        graph.add_vertex("F")
        graph.add_edge("E", "F")

        self.assertEqual(5, graph.num_vertices)
        self.assertEqual(3, graph.num_edges)
        self.assertCountEqual(["A", "B", "C", "E", "F"], graph.get_vertices())

    def test_find_fastest_route(self):
        pass

    def test_busiest_intersection(self):
        pass

    def test_find_near_me(self):
        pass
