# Directed_graph_comparison
Directed weighted graph implement in python in order to make a comparison with out Java project and Networkx lib.

# About our project
this project is a follow-up project to the previous one's.
this project is build about 3 main algorithms: shortest_path, connected component and connected components.

the goal for this project is to implement an directed weighted graph (data structre), in python, and then make a comparison
with our java project (compar the Run times and results), also we make compar with python Networkx graph lib.

# How the graph is build?
in our project there is "DiGraph" class, that implement the graph itself.
in additional to DiGraph, there are also NodeData and EdgeData classes that represent a Node and Edge in our graph. 

 *DiGraph*:
 
 Class that implements the 'interface' "GraphInterface" which represents a directed weighted graph.
 our graph contain dictionary on nodes and edges.
 
 **v_size()** : return the number of nodes in the graph.
 
 **e_size()** : return the number of edges in the graph.
 
 **get_all_v()** : return dictionary of all the nodes in the graph.
 
 **all_in_edges_of_node(id1)** : return a dictionary (key,weight) of the nodes that connected starting from node id1.
 
 **all_out_edges_of_node(id1)** : return a dictionary (key,weight) of all the nodes that connected from id1.
 
 **add_node(node_id, pos)** : add a node into the graph with given id and position.
 
 **add_edge(id1, id1, weight) : add edge between id1 and id2 with the givin weight.
 
 **get_mc()** : return the number of changes that were make in out graph.
 
 **remove_node(id1)** : remove node id1 from the graph
 
 **remove_edge(id1, id2) : remove the edge between id1 and id2 
 
 
 *GraphAlgo* 
