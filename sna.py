import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

twitch_data = pd.read_csv('data/large_twitch_features.csv')

# Display the first few rows of the dataframe
print(twitch_data.head())