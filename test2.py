# 1. Import the essential libraries
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

from itertools import combinations
def get_combinations(input_list):
    """
    Generate all possible combinations of pairs within a list.
    Args:
        input_list (list): The input list.
    Returns:
        list: A list of tuples representing all possible combinations of pairs.
    """
    combinations_list = list(combinations(input_list, 2))
    return combinations_list



# 2. Create two lists of band members
smashing_pumpkins = ['Billy Corgan',
                    'James Iha', 
                    'Jimmy Chamberlin',
                    'Katie Cole',
                    'D\'arcy Wretzky', 
                    'Melissa Auf der Maur', 
                    'Ginger Pooley', 
                    'Mike Byrne',
                    'Nicole Fiorentino']

zwan = ['Billy Corgan', 
        'Jimmy Chamberlin', 
        'Paz Lenchantin', 
        'David Pajo', 
        'Matt Sweeney']





pumkin_tuples = get_combinations(smashing_pumpkins)
zwan_tuples = get_combinations(zwan)
# Combine the lists of tuples
band_members = pumkin_tuples + zwan_tuples
# Remove any doubles like ('Billy Corgan', 'Billy Corgan')
band_members = [b for b in band_members if b[0] != b[1]]

G_symmetric = nx.Graph()
for pair in band_members:
    G_symmetric.add_edge(pair[0], pair[1])
    
fig = plt.figure(figsize=(8, 6))
nx.draw_networkx(G_symmetric)
plt.show()

# 1. Use methods in NetworkX to extract centrality measures
betweenness_centrality = nx.betweenness_centrality(G_symmetric)
degree_centrality = nx.degree_centrality(G_symmetric)

# 2. Calculate betweenness, and store values in a dataframe
bc_data = pd.DataFrame.from_dict(betweenness_centrality, 
                                 columns=["BetweennessCentrality"], 
                                 orient="index")

# 3. Calculate betweenness, and store values in a dataframe
dc_data = pd.DataFrame.from_dict(degree_centrality, 
                                 columns=["DegreeCentrality"], 
                                 orient="index")

# 4. Calculate betweenness, and store values in a dataframe
centrality_data = pd.concat([bc_data, dc_data], axis=1)

# 5. Print the centrality data
print(centrality_data)