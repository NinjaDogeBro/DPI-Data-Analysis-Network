import networkx as nx
import pandas as pd
import matplotlib

# create a new graph
G_symmetric = nx.Graph()

# add edges to the graph
G_symmetric.add_edge('Billy Corgan','James Iha')
G_symmetric.add_edge('Billy Corgan','D\'arcy Wretzky')
G_symmetric.add_edge('Billy Corgan','Jimmy Chamberlin')

# calculate degree centrality and betweenness for nx
degree_centrality = nx.degree_centrality(G_symmetric)
betweenness_centrality = nx.betweenness_centrality(G_symmetric)

# define the node labels
nodes  = ["Billy Corgan", "James Iha", "D'arcy Wretzky", "Jimmy Chamberlin"]

# retrieve degree centrality for each node
dc_calculations = []
bc_calculations = []

for node in nodes:
    dc_calculations += [degree_centrality[node]]
    bc_calculations += [betweenness_centrality[node]]

# create a centrality data df to store values
centrality_data = pd.DataFrame()

# populate the df with the nodes and their centrality values
centrality_data["Node"] = nodes
centrality_data["Degree-Centrality"] = dc_calculations
centrality_data["Betweenness-Centrality"] = bc_calculations

print(dc_calculations)
print(bc_calculations)
# print the centrality data