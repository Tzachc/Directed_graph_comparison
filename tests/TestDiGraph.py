from unittest import TestCase
from DiGraph import DiGraph


class TestDiGraph(TestCase):

    def test_empty_graph(self):
        graph = DiGraph()
        self.assertTrue(graph.edgeCounter == 0)
        self.assertTrue(graph.MC == 0)
        self.assertTrue(graph.nodes.__len__() == 0)

    def test_add_node(self):
        graph = DiGraph()
        self.assertTrue(graph.nodes.__len__() == 0)
        graph.add_node(1)
        self.assertTrue(graph.nodes.__len__() == 1)
        graph.add_node(2)
        self.assertTrue(graph.nodes.__len__() == 2)
        for i in range(5):
            graph.add_node(i)
        self.assertTrue(graph.nodes.__len__() == 5)

    def test_add_edges(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        self.assertEqual(0, graph.edgeCounter)
        graph.add_edge(0,1,23)
        self.assertTrue(1,graph.edgeCounter)
        graph.add_edge(0, 1, 222) # add an edge that's exits
        self.assertTrue(1,graph.edgeCounter)
        graph.add_edge(1,0,20)
        graph.add_edge(2,1,76)
        self.assertTrue(3, graph.edgeCounter)
        graph.remove_node(2)
        self.assertTrue(2,graph.edgeCounter)

    def test_remove_nodes(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        self.assertEqual(10,graph.nodes.__len__())
        graph.remove_node(4)
        self.assertEqual(9,graph.nodes.__len__())

    def test_remove_edges(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        graph.add_edge(0,1,20)
        graph.add_edge(1,2,33)
        graph.add_edge(0,5,44)
        graph.add_edge(5,7,76)
        self.assertEqual(4,graph.edgeCounter)
        self.assertEqual(10,graph.nodes.__len__())
        graph.remove_edge(0,1)
        self.assertEqual(3,graph.edgeCounter)
        self.assertEqual(10, graph.nodes.__len__())
