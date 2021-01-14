import math
from collections import deque
from random import random
from typing import List
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import json
from GraphAlgoInterface import GraphAlgoInterface
from queue import PriorityQueue, Queue
import matplotlib.pyplot as plt
import random
from src import NodeData
import numpy


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """in this method we get a string name, and load a JSON file with the given name
        into a graph"""
        new_graph = DiGraph()
        try:
            with open(file_name, "r") as f:
                new_dict = json.load(f)
                for i in new_dict["Nodes"]:
                    key = -1
                    pos = None
                    for k, v in i.items():
                        if k == "pos":
                            pos = v
                        elif k == "id":
                            key = v
                    if pos is not None:
                        tup_from_string = tuple(pos.split(","))
                        new_tuple = (float(tup_from_string[0]), float(tup_from_string[1]), float(tup_from_string[2]))
                        new_graph.add_node(key, new_tuple)
                        pos = None
                    else:
                        new_graph.add_node(key, None)
                for i in new_dict["Edges"]:
                    src = -1
                    weight = -1
                    dest = -1
                    for k, v in i.items():
                        if k == "src":
                            src = v
                        elif k == "dest":
                            dest = v
                        else:
                            weight = v
                    new_graph.add_edge(src, dest, weight)
            self.graph = new_graph
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """ in this method we save the current graph into a JSOn file
        with the given name.
        """
        if self.graph is None or len(self.graph.nodes) == 0:
            return False
        Nodes = []
        Edges = []
        for node in self.graph.get_all_v().values():
            if node.get_pos() is not None:
                Nodes.append(
                    {"pos": "" + str(node.get_pos()[0]) + "," + str(node.get_pos()[1]) + "," + str(node.get_pos()[2]),
                     "id": node.get_id()})
            else:
                Nodes.append({"id": node.get_id()})
            for dest, edges in self.graph.all_out_edges_of_node(node.get_id()).items():
                Edges.append({"src": node.get_id(), "w": edges, "dest": dest})
        graph_to_json = {"Edges": Edges, "Nodes": Nodes}
        try:
            with open(file_name, "w") as f:
                json.dump(graph_to_json, default=lambda o: o.__dict__, indent=4, fp=f)
                return True
        except Exception as e:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        find the shortest_path (weight wise) between node id1 and node id2
        based on dijkstra algorithm.
        return the weight and list of the actuall path. (sum_weight, [id1-->...->id2])
        """
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return float('inf'), []
        if self.graph is None:
            return float('inf'), []
        self.init_dijkstra()
        q = PriorityQueue()
        nodes = self.graph.get_all_v()
        node = nodes[id1]
        node.weight = 0
        q.put((node.weight, node))

        while not q.empty():
            temp = q.get()[1]
            for edge in self.graph.all_out_edges_of_node(temp.get_id()).values():
                u = nodes[edge.get_dest()]
                dist = edge.get_weight() + temp.weight
                if dist < u.weight:
                    u.weight = dist
                    u.info = temp.get_id()
                    q.put((u.weight, u))
        dest = nodes[id2]

        if self.is_finish(dest):
            return float('inf'), []
        path = self.get_actuall_path(self.graph, dest)
        return dest.weight, path

    def get_actuall_path(self, graph: DiGraph, dest: NodeData):
        """
        helper method to get the actually [id1-->...->id2]
        """
        path = [dest.get_id()]
        dest_info = dest.info
        while dest_info != "white" and dest is not None:
            node = graph.get_all_v()[dest_info]
            path.insert(0, node.get_id())
            dest_info = node.info
        return path

    def is_finish(self, dest) -> bool:
        infinity = math.inf
        if dest.weight is infinity:
            return True

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component that node id1 is a part of.
        param id1: The node id
        return: list of nodes in the SCC
        """
        if id1 not in self.graph.get_all_v():
            return []
        if self.get_graph() is None:
            return []
        reverse = DiGraph()
        dq = deque()
        the_connections = self.bfs(id1, reverse, dq, self.graph)
        dq.append(id1)
        reverse_connections = self.bfs(id1, self.graph, dq, reverse)
        return list(set(the_connections) & set(reverse_connections))

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component in the graph.
        return: The list all strongly connected componenet
        """
        if self.graph is None:
            return []
        nodes = self.graph.get_all_v()
        keys = nodes.keys()
        ans = []
        connected = []
        for key in keys:
            if key not in connected:
                key_connected = self.connected_component(key)
                connected.extend(key_connected)
                ans.append(key_connected)
        return ans

    def plot_graph(self) -> None:
        """
        plot the graph
        """
        x, y = [], []
        nodes = self.graph.get_all_v()
        for node in nodes.values():
            if node.get_pos() is None:
                node.set_pos((random.random() * 100, random.random() * 100, 0))
            x.append(node.get_pos()[0])
            y.append(node.get_pos()[1])

        width_graph = self.graph_width(nodes)
        heith_graph = self.graph_height(nodes)
        x_min = width_graph[0]
        x_max = width_graph[1]
        y_min = heith_graph[0]
        y_max = heith_graph[1]
        normal_x = lambda i: (i - x_min) / (x_max - x_min)
        normal_y = lambda i: (i - y_min) / (y_max - y_min)
        x = [normal_x(i) for i in x]
        y = [normal_y(i) for i in y]

        fig, ax = plt.subplots(figsize=(10, 7))

        ax.scatter(x, y, color='yellow', linewidths=1, edgecolors='blue', s=150)
        ax.set_xticks([])
        ax.set_yticks([])
        for node in self.graph.get_all_v().values():
            x1, y1 = normal_x(node.get_pos()[0]), normal_y(node.get_pos()[1])
            ax.annotate(node.get_id(), (x1, y1 + 0.012), size=15)
            for dest, nei in self.graph.all_out_edges_of_node(node.get_id()).items():
                x2, y2 = normal_x(self.graph.nodes.get(dest).get_pos()[0]), normal_y(
                    self.graph.nodes.get(dest).get_pos()[1])
                ax.arrow(x1, y1, x2 - x1, y2 - y1, length_includes_head=True, color='black', head_width=0.01)
        plt.axis('off')
        plt.show()

    def init_dijkstra(self):
        for node in self.graph.get_all_v().values():
            node.weight = math.inf
            node.tag = 0
            node.info = "white"

    def bfs(self, id1: int, reverse_graph: DiGraph, q: deque, graph: DiGraph) -> list:
        """
        helper method for the connected componenet, bfs algorithm impelement.
        """
        q.append(id1)
        connected = {id1: True}
        the_connect_list = [id1]
        reverse_graph.add_node(id1)
        while len(q) != 0:
            curr = q.popleft()
            curr_edges = graph.all_out_edges_of_node(curr)
            for curr_ni in curr_edges.keys():
                reverse_graph.add_node(curr_ni)
                reverse_graph.add_edge(curr_ni, curr, curr_edges.get(curr_ni))
                if connected.get(curr_ni) is None:
                    q.append(curr_ni)
                    connected[curr_ni] = True
                    the_connect_list.append(curr_ni)
        return the_connect_list

    def graph_width(self, v_dict: dict):
        """
        helper method for the plot method, give us the min and max values
        for X and return a list of those values's
        """
        min_val = float('inf')
        max_val = -1
        for k, v in v_dict.items():
            if v.get_pos() is not None:
                v2 = v.get_pos()[0]
                if v2 < min_val:
                    min_val = v2
                elif v2 > max_val:
                    max_val = v2
        width = [min_val, max_val]
        return width

    def graph_height(self, v_dict: dict):
        """
        helper method for the plot method, give us the min and max values
        for Y and return a list of those values's
        """
        min_val = float('inf')
        max_val = -1
        for k, v in v_dict.items():
            if v.get_pos() is not None:
                v2 = v.get_pos()[1]
                if v2 < min_val:
                    min_val = v2
                elif v2 > max_val:
                    max_val = v2
        height = [min_val, max_val]
        return height
