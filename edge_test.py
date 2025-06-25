import networkx as nx
import pandas as pd
import matplotlib
import random

# create a new graph
G_symmetric = nx.Graph()

# add edges to the graph
G_symmetric.add_edge('Billy Corgan','James Iha')
G_symmetric.add_edge('Billy Corgan','D\'arcy Wretzky')
G_symmetric.add_edge('Billy Corgan','Jimmy Chamberlin')

# Test to grab random edge
random_edge = random.choice(list(G_symmetric.edges()))

print("Randomly selected edge:", random_edge)