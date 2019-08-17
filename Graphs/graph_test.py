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

    def test_find_fastest_route(self):
        pass

    def test_busiest_intersection(self):
        pass

    def test_find_near_me(self):
        pass
