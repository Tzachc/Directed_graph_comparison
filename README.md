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

 ***DiGraph***:
 
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
 
 
 ***GraphAlgo*** 
 
 graphAlgo class implements the interface "GraphAlgoInterface" and represent the algorithms that can be used in our 
 directed graph.
 
 **get_graph()** : return the graph.
 
 **load_from_json(file_name)** : the method recevie a string name of a graph that saved in JSON format, and loat it into graph.
 
 **save_to_json(file_name)** : save the graph into JSON format, with the given name.
 
 **shortest_path(id1,id2)** : this method find the cheapest way (weights) to get from id1 to id2, used with dijkstra algorithm.
 the method return the cost (the weight in total) and the path iteself like (id1 --> .. --> id2).
 
 **get_actuall_path**(graph, dest : NodeData)** : helper method for the shortest_path to get the actuall path.
 
 **connected_component(id1)** : give us a list with id's of the nodes which are part of strongly connected component of our id1.
 
 **connected_components()** : return list of all strongly connected component in our graph.
 
 **plot_graph()** : plot the graph.
 
 **bfs(id1, reverse_graph, dequeu, graph)->list** : helper method BFS used for the connected_component check.
 
 **graph_width(dict)** : return a list of the smallest x and the highest x values for use in the plot_graph method.
 
 **graph_height(dict)** : return a list of the smallest y and the highest y values for use in the plot_graph method.
 
 
