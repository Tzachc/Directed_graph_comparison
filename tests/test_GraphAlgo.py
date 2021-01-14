from unittest import TestCase
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from src import DiGraph
from src import GraphAlgo

class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        graph = DiGraph()
        for i in range(0, 7):
            graph.add_node(i)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph_algo.get_graph(), graph)

    def test_connected_component(self):
        graph = DiGraph()
        for i in range(0, 5):
            graph.add_node(i)
        graph.add_edge(0, 1, 10)
        graph.add_edge(0, 2, 3)
        graph.add_edge(2, 0, 3)
        graph.add_edge(2, 3, 4)
        graph.add_edge(3, 2, 4)
        graph.add_edge(3, 1, 1)
        graph.add_edge(1, 3, 1)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph_algo.connected_component(3), [0,1,2,3])
        self.assertEqual(graph_algo.connected_component(4), [4])
    def test_connected_components(self):
        graph = DiGraph()
        for i in range(0, 5):
            graph.add_node(i)
        graph.add_edge(0, 1, 10)
        graph.add_edge(1,0, 20)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph_algo.connected_components(),[[0,1], [2], [3], [4]])
        graph.add_edge(0, 2, 32)
        self.assertEqual(graph_algo.connected_components(),[[0,1], [2], [3], [4]])
        graph.add_edge(2,0, 50)
        self.assertEqual(graph_algo.connected_components(), [[0, 1 , 2],[3], [4]])
        graph.add_edge(2,4,6)
        graph.add_edge(4,3,545)
        graph.add_edge(1,3,43)
        graph.add_edge(3,1,2)
        print(graph_algo.connected_components())
        self.assertEqual(graph_algo.connected_components(), [[0,1,2,3,4]])

    def test_shortest_path(self):
        graph = DiGraph()
        for i in range(0, 5):
            graph.add_node(i)
        graph.add_edge(0, 1, 10)
        graph.add_edge(1, 0, 20)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph_algo.shortest_path(0,1) , (10, [0,1]))
        graph.add_edge(1,2 , 3.5)
        graph.add_edge(0, 2, 32)
        self.assertEqual(graph_algo.shortest_path(0,2), (13.5, [0, 1, 2]))

    def test_shortest_path_inf(self):
        graph = DiGraph()
        for i in range(0, 5):
            graph.add_node(i)
        graph.add_edge(0, 1, 2)
        graph.add_edge(2, 3, 2)
        graph_algo = GraphAlgo(graph)
        expected = (0, [0])
        self.assertEqual(graph_algo.shortest_path(0, 0), (0, [0]))
        self.assertEqual(graph_algo.shortest_path(1, 0), (float('inf'), []))

    def test_save_load(self):
        graph = DiGraph()
        for i in range(0, 6):
            graph.add_node(i)
        graph.add_edge(0, 1, 2)
        graph.add_edge(1, 0, 1)
        graph.add_edge(1, 3, 3)
        graph.add_edge(1, 2, 8)
        graph.add_edge(1, 5, 10)

        graph_algo = GraphAlgo(graph)
        graph_algo.save_to_json('json_graph')
        graph_algo2 = GraphAlgo()
        graph_algo2.load_from_json('json_graph')
        graph_algo3 = GraphAlgo()
        graph_algo3.load_from_json("../data/A5")
        self.assertTrue(graph_algo.graph.__eq__(graph_algo2.graph))

    def test_plot_graph(self):
        graph_algo2 = GraphAlgo()
        graph_algo2.load_from_json("../data/G_10_80_1.json")
        graph_algo2.plot_graph()