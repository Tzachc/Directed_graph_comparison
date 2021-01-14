import json
import random
import time
import unittest
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph


def current_time() -> int:
    millseconds = int(round(time.time() * 1000))
    return millseconds


def load_graph_from_nx(path: str) -> nx.DiGraph:
    path_str = path
    with open(path_str, 'r') as file:
        s = json.load(file)
    g = nx.DiGraph()
    for node in s["Nodes"]:
        g.add_node(node['id'])
    for edge in s["Edges"]:
        g.add_edge(edge["src"], edge["dest"], w=edge["w"])
    return g


class test_compration(unittest.TestCase):

    def test_shortest_path(self):
        p = "../data/G_10_80_0.json"
        p1 = "../data/G_100_800_0.json"
        p2 = "../data/G_1000_8000_0.json"
        p3 = "../data/G_10000_80000_0.json"
        p4 = "../data/G_20000_160000_0.json"
        p5 = "../data/G_30000_240000_0.json"
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(p)
        g = load_graph_from_nx(p)
        start = current_time()
        graph_algo.shortest_path(1, 5)
        end = current_time()
        print("My shortest_path took : ", end - start , "of graph p")
        start = current_time()
        nx.shortest_path(g, 1, 5, method='dijkstra')
        end = current_time()
        print("Networkx shortest_path took : " , end - start, "of graph p")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p1)
        g = load_graph_from_nx(p1)
        start = current_time()
        graph_algo.shortest_path(1, 500)
        end = current_time()
        print("My shortest_path took : ", end - start, "of graph p1")
        start = current_time()
        nx.shortest_path(g, 10, 50, method='dijkstra')
        end = current_time()
        print("Networkx shortest_path took : ", end - start, "of graph p1")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p2)
        g = load_graph_from_nx(p2)
        start = current_time()
        graph_algo.shortest_path(10, 50)
        end = current_time()
        print("My shortest_path took : ", end - start, "of graph p2")
        start = current_time()
        nx.shortest_path(g, 10, 50, method='dijkstra')
        end = current_time()
        print("Networkx shortest_path took : ", end - start, "of graph p2")

        print("--------------------------------------------------")
        graph_algo.load_from_json(p3)
        g = load_graph_from_nx(p3)
        start = current_time()
        graph_algo.shortest_path(10, 50)
        end = current_time()
        print("My shortest_path took : ", end - start, "of graph p3")
        start = current_time()
        nx.shortest_path(g, 10, 50, method='dijkstra')
        end = current_time()
        print("Networkx shortest_path took : ", end - start, "of graph p3")

        print("--------------------------------------------------")
        graph_algo.load_from_json(p4)
        g = load_graph_from_nx(p4)
        start = current_time()
        graph_algo.shortest_path(10, 50)
        end = current_time()
        print("My shortest_path took : ", end - start, "of graph p4")
        start = current_time()
        nx.shortest_path(g, 10, 50, method='dijkstra')
        end = current_time()
        print("Networkx shortest_path took : ", end - start, "of graph p4")

        print("--------------------------------------------------")
        graph_algo.load_from_json(p5)
        g = load_graph_from_nx(p5)
        start = current_time()
        graph_algo.shortest_path(10, 50)
        end = current_time()
        print("My shortest_path took : ", end - start, "of graph p5")
        start = current_time()
        nx.shortest_path(g, 10, 50, method='dijkstra')
        end = current_time()
        print("Networkx shortest_path took : ", end - start, "of graph p5")

    def test_connected_components(self):
        p = "../data/G_10_80_0.json"
        p1 = "../data/G_100_800_0.json"
        p2 = "../data/G_1000_8000_0.json"
        p3 = "../data/G_10000_80000_0.json"
        p4 = "../data/G_20000_160000_0.json"
        p5 = "../data/G_30000_240000_0.json"
        graph_algo = GraphAlgo()

        graph_algo.load_from_json(p)
        g = load_graph_from_nx(p)
        start = current_time()
        graph_algo.connected_components()
        end = current_time()
        print("My connected_components took : ", end - start, "of graph p")
        start = current_time()
        nx.kosaraju_strongly_connected_components(g)
        end = current_time()
        print("Networkx connected_components took : ", end - start, "of graph p")
        print("--------------------------------------------------")

        graph_algo.load_from_json(p1)
        g = load_graph_from_nx(p1)
        start = current_time()
        graph_algo.connected_components()
        end = current_time()
        print("My connected_components took : ", end - start, "of graph p1")
        start = current_time()
        nx.kosaraju_strongly_connected_components(g)
        end = current_time()
        print("Networkx connected_components took : ", end - start, "of graph p1")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p2)
        g = load_graph_from_nx(p2)
        start = current_time()
        graph_algo.connected_components()
        end = current_time()
        print("My connected_components took : ", end - start, "of graph p2")
        start = current_time()
        nx.kosaraju_strongly_connected_components(g)
        end = current_time()
        print("Networkx connected_components took : ", end - start, "of graph p2")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p3)
        g = load_graph_from_nx(p3)
        start = current_time()
        graph_algo.connected_components()
        end = current_time()
        print("My connected_components took : ", end - start, "of graph p3")
        start = current_time()
        nx.kosaraju_strongly_connected_components(g)
        end = current_time()
        print("Networkx connected_components took : ", end - start, "of graph p3")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p4)
        g = load_graph_from_nx(p4)
        start = current_time()
        graph_algo.connected_components()
        end = current_time()
        print("My connected_components took : ", end - start, "of graph p4")
        start = current_time()
        nx.kosaraju_strongly_connected_components(g)
        end = current_time()
        print("Networkx connected_components took : ", end - start, "of graph p4")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p5)
        g = load_graph_from_nx(p5)
        start = current_time()
        graph_algo.connected_components()
        end = current_time()
        print("My connected_components took : ", end - start, "of graph p5")
        start = current_time()
        nx.kosaraju_strongly_connected_components(g)
        end = current_time()
        print("Networkx connected_components took : ", end - start, "of graph p5")

    def test_connected_component(self):
        p = "../data/G_10_80_0.json"
        p1 = "../data/G_100_800_0.json"
        p2 = "../data/G_1000_8000_0.json"
        p3 = "../data/G_10000_80000_0.json"
        p4 = "../data/G_20000_160000_0.json"
        p5 = "../data/G_30000_240000_0.json"
        graph_algo = GraphAlgo()

        graph_algo.load_from_json(p)
        g = load_graph_from_nx(p)
        start = current_time()
        graph_algo.connected_component(3)
        end = current_time()
        print("My connected_component took : ", end - start, "of graph p")
        print("--------------------------------------------------")

        graph_algo.load_from_json(p1)
        g = load_graph_from_nx(p1)
        start = current_time()
        graph_algo.connected_component(3)
        end = current_time()
        print("My connected_component took : ", end - start, "of graph p1")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p2)
        g = load_graph_from_nx(p2)
        start = current_time()
        graph_algo.connected_component(3)
        end = current_time()
        print("My connected_component took : ", end - start, "of graph p2")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p3)
        g = load_graph_from_nx(p3)
        start = current_time()
        graph_algo.connected_component(3)
        end = current_time()
        print("My connected_component took : ", end - start, "of graph p3")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p4)
        g = load_graph_from_nx(p4)
        start = current_time()
        graph_algo.connected_component(3)
        end = current_time()
        print("My connected_component took : ", end - start, "of graph p4")

        print("--------------------------------------------------")

        graph_algo.load_from_json(p5)
        g = load_graph_from_nx(p5)
        start = current_time()
        graph_algo.connected_component(3)
        end = current_time()
        print("My connected_component took : ", end - start, "of graph p5")
