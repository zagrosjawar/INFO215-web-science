import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G = nx.karate_club_graph()

# Print out the list of nodes and edges with attributes.
print(G.nodes(data=True))
print("--------------------")
print(G.edges(data=True))
# or as a dictionary
# print(dict(G.nodes))
# print(dict(G.edges))


# providing a visualization of the Karate club where
# the color of nodes will represent the two groups after the separation.
degrees = G.degree()
# print(degrees)
node_colors = []
for node in G.nodes():
    if G.nodes[node]["club"] == "Mr. Hi":
        node_colors.append("Orange")
    else:  # Officer
        node_colors.append("Lightblue")

node_sizes = np.asarray([degrees[node]*60 for node in G.nodes()])
# print(node_sizes)

options = {
    "node_color": node_colors,
    "node_size": node_sizes,
    #"cmap": plt.cm.RdGy,
    "edge_color": "lightblue",
    "linewidths": 0,
    "width": 0.4,
    "with_labels": True
}

pos = nx.spring_layout(G)
nx.draw(G, pos, **options)
plt.show()

# using nx.dikstra_path()
path = nx.dijkstra_path(G, source=24, target=16, weight="weight")
print(path)

# Provide a visualization of the Karate club and modify the color of the nodes by highlighting
# the selected nodes from the above list (dijkstra-path).
# Use red color to indicate the selection of the nodes.


degrees = G.degree()
# print(degrees)
node_colors = []
for node in G.nodes():
    if node in path:
        node_colors.append("red")
        continue

    if G.nodes[node]["club"] == "Mr. Hi":
        node_colors.append("Orange")
    else:  # Officer
        node_colors.append("Lightblue")

node_sizes = np.asarray([degrees[node]* 60 for node in G.nodes()])
# print(node_sizes)

options = {
    "node_color": node_colors,
    "node_size": node_sizes,
    #"cmap": plt.cm.RdGy,
    "edge_color": "lightblue",
    "linewidths": 0,
    "width": 0.5,
    "with_labels": True
}

pos = nx.spring_layout(G)
nx.draw(G, pos, **options)
plt.show()




