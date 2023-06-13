import networkx as nx
import csv
import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# working with network centrality and modularity using NetworkX library.
# The details are given below:
# 1.1 Load a graph using networkx library from the following csv file: 'nutrients.csv'

with open("nutrients.csv", "r") as file:
    reader = csv.reader(file)
    G = nx.Graph(reader)
    print(G.nodes())  # list

# 1.2 Measure centrality based on degree/eigenvector centrality using networkx library.
# dict {'node': degree}
degree_centrality = nx.degree_centrality(G)
# dict
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=100, tol=1e-06, nstart=None, weight=None)
print("degree centrality", degree_centrality)
print("eigenvector centrality", eigenvector_centrality)

# 1.3 Detect modularity of the graph using label propagation or louvain method (use networkx libraries).
# Remember: partition is a set of communities C = {S, T}
# dict {'A': 0,'green leafy vegs': 1, 'liver': 3, 'milk': 0, 'tomatoes': 2, 'B12': 3, 'B6': 3}
partition = community_louvain.best_partition(G)  # dict
print("Partition:", partition)

# 1. 4 Modify the size and color based on the above measures.
# 1. 5 Use spring layout or fruchterman_reingold layout for visualizing the graph.

# color -->the nodes according to their partition
cmap = cm.get_cmap("viridis", max(partition.values()) + 1)

# size
sizes = []  # or [deg * 2000 for deg in degree_centrality.values()]
for i in degree_centrality.values():
    sizes.append(i * 2000)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=partition.keys(), node_size=sizes, node_color=list(partition.values()),
                       cmap=cmap)
nx.draw_networkx_labels(G, pos, labels={n: n for n in G.nodes()}, font_size=10, font_color="black", font_weight="bold")
nx.draw_networkx_edges(G, pos, alpha=0.5)

plt.show()
