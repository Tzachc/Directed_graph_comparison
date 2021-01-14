from GraphInterface import GraphInterface
from NodeData import NodeData
from EdgeData import EdgeData
from typing import Dict
import math


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes: Dict[int, NodeData] = dict()
        self.edges: Dict[int, Dict[int, EdgeData]] = dict()
        self.edgeCounter = 0
        self.MC = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary(key,weight) of the nodes that connected
        starting from node id1.
        """
        temp_edge_grah: Dict[int, EdgeData] = dict()
        for i in self.nodes:
            if id1 in self.edges.get(i):
                temp_edge_grah.__setitem__(i, self.edges.get(i)[id1])
        return temp_edge_grah

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary(key,weight) of all the nodes that connected from id1.
        """
        edges_graph: Dict[int, EdgeData] = dict()
        if id1 in self.nodes:
            for temp in self.edges.get(id1):
                edges_graph.__setitem__(temp, self.edges.get(id1)[temp])
        return edges_graph

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        add edge between id1 and id2 with the givin weight.
        """
        if id2 in self.edges.get(id1):
            return False
        if id1 == id2:
            return False
        if self.edges.__contains__(id1) and self.edges.__contains__(id2):
            self.edges.get(id1).update({id2: EdgeData(id1, id2, weight)})
            self.edgeCounter += 1
            self.MC += 1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        add a node into the graph with given id and position.
        """
        if self.nodes.__contains__(node_id):
            return False
        else:
            node_to_add = NodeData(node_id, pos)
            self.nodes.update({node_id: node_to_add})
            self.edges.update({node_id: dict()})
            self.MC += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        """ remove node id1 from the graph"""
        if node_id not in self.nodes:
            return False
        if self.nodes.__contains__(node_id):
            node_to_remove = self.nodes.get(node_id)
            self.edgeCounter -= len(self.edges.get(node_id).values())
            self.MC += len(self.edges.get(node_id).values()) + 1
            for i in self.all_in_edges_of_node(node_id):
                self.edges.get(i).pop(node_id)
                self.edgeCounter -= 1
            self.edges.pop(node_id)
            self.nodes.pop(node_id)
            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        remove the edge between id1 and id2
        """
        if node_id1 == node_id2:
            return False
        if self.edges.get(node_id1).__contains__(node_id2):
            self.edges.get(node_id1).pop(node_id2)
            self.MC += 1
            self.edgeCounter -= 1
            return True
