from dwave.system import LeapHybridSampler
import dwave_networkx as dnx
import networkx as nx
import random

# Create a hybrid solver
solver = LeapHybridSampler()

# Create a random graph where nodes are connected based on distance and set the weights to 1 or -1
problem_node_count = 30
G = nx.random_geometric_graph(problem_node_count, radius=0.0005*problem_node_count)
G.add_edges_from([(u, v, {'sign': random.choice((-1, 1))}) for u, v in G.edges])

imbalance, bicoloring = dnx.structural_imbalance(G, solver)
set1 = int(sum(list(bicoloring.values())))
print("One set has {} nodes; the other has {} nodes.".format(set1, problem_node_count-set1))  
print("The network has {} frustrated relationships.".format(len(list(imbalance.keys()))))  