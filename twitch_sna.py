import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random
import os
import json
from networkx.readwrite import json_graph

# This will be used to ensure multiple saves for the 2 graphs we are saving
from datetime import datetime
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Creating a new folder for each execution to save the graph, histogram, and txt file
os.makedirs(f'multiverse/run_{timestamp}', exist_ok=True)

# Creating a txt file to save the output
output_file = open(f'multiverse/run_{timestamp}/twitch_sna_output_{timestamp}.txt', 'w')

twitch_data_edges = pd.read_csv('data/musae_ENGB_edges.csv')
twitch_data_target = pd.read_csv('data/musae_ENGB_target.csv')

graph = nx.Graph()

# Add edges to the graph from the edges dataframe
graph = nx.from_pandas_edgelist(twitch_data_edges, source='from', target='to')

# Add nodes to the graph from the target dataframe
random_people = [random.choice(list(graph.edges()))]  # To start, randomly select an edge and put it in a list

while len(random_people) < 30:  # Ensure we have at least 30 random edges
    # Randomly select another edge from the graph
    random_edge = random.choice(list(graph.edges()))
    # Check if the edge is not already in the list of random people and one of the people
    # is a connection to another edge
    if random_edge not in random_people:
        # Check if either node of the edge is already in the list of random people
        # If so, add the edge to the list of random people
        for edge in random_people:
            if (random_edge[0] == edge[0] or random_edge[1] == edge[0]) or (random_edge[0] == edge[1] or random_edge[1] == edge[1]):
                random_people.append(random_edge)
                break

# Create a new graph to hold the filtered edges
# This will contain only the edges that connect to the random people
filtered_graph = nx.Graph()

# Add the filtered edges to the new graph
for i in range(len(random_people)):
    filtered_graph.add_edge(random_people[i][0], random_people[i][1])

# Calculate degree centrality and betweenness centrality
degree_centrality = nx.degree_centrality(filtered_graph)
betweenness_centrality = nx.betweenness_centrality(filtered_graph)

# Display the first few rows of the dataframe
# print(twitch_data_edges.head())
# print(twitch_data_target.head())
output_file.write("Twitch Social Network Analysis Output\n")
output_file.write("Processing Twitch data...\n\n")

# Save the degree and betweenness centrality to JSON format
deg_central_file = open(f'multiverse/run_{timestamp}/JSON_deg_central_twitch_{timestamp}.txt', 'w')
bet_central_file = open(f'multiverse/run_{timestamp}/JSON_bet_central_twitch_{timestamp}.txt', 'w')

# Make sure to convert the dictionaries to JSON format
dict_deg_central = json.dumps(degree_centrality, indent=4)
dict_bet_central = json.dumps(betweenness_centrality, indent=4)

# Write the JSON data to the files
deg_central_file.write(dict_deg_central)
bet_central_file.write(dict_bet_central)

deg_central_file.close()
bet_central_file.close()

rank = 1

output_file.write("Degree Centrality Top 3 leaderboard:\n")
top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse= True)[:3]
for node, centrality in top_degree:
    output_file.write(f"#{rank} Person {node}: {centrality:.4f}\n")
    rank += 1

rank = 1

output_file.write("\nBetweenness Centrality Top 3 leaderboard:\n")
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse= True)[:3]
for node, centrality in top_betweenness:
    output_file.write(f"#{rank} Person {node}: {centrality:.4f}\n")
    rank += 1

# Draw the filtered graph
fig = plt.figure(figsize=(8, 6))
nx.draw_networkx(filtered_graph, with_labels=True, node_size=50, font_size=8) # Make spider web graph
# Save the graph as an image file
fig.savefig(f'multiverse/run_{timestamp}/twitch_sna_graph_{timestamp}.png', dpi=300, bbox_inches='tight')
plt.show()


# Save the graph in JSON format
data = json_graph.node_link_data(filtered_graph)  # Convert the graph to a JSON
# format
with open(f'multiverse/run_{timestamp}/JSON_graph_twitch_{timestamp}.json', 'w') as f:
    json.dump(data, f)  # Write the JSON data to a file

# Draw the histogram of the degree distribution
degree_sequence = [d for n, d in filtered_graph.degree()]  # Get the degree sequence

fig = plt.figure(figsize=(10, 6))  # Set the figure size
plt.hist(degree_sequence, bins=range(min(degree_sequence), max(degree_sequence) + 2), align='left') # Plot the histogram
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")
plt.title("Degree Distribution")
# Save the histogram as an image file
plt.savefig(f'multiverse/run_{timestamp}/twitch_sna_histogram_{timestamp}.png', dpi=300, bbox_inches='tight')
plt.show()


output_file.write("\nGraph drawn successfully.")