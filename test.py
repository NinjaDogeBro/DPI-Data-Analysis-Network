import networkx as nx
import matplotlib.pyplot as plt

# create a new graph
G_symmetric = nx.Graph()

# add nodes and edges
G_symmetric.add_edge('Billy Corgan','James Iha')
G_symmetric.add_edge('Billy Corgan','D\'arcy Wretzky')
G_symmetric.add_edge('Billy Corgan','Jimmy Chamberlin')

# draw the graph
fig = plt.figure(figsize=(12, 8))
nx.draw_networkx(G_symmetric, font_size=10)
plt.show()