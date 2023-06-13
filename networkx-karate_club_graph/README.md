# NetworkX Karate Club Graph

This program utilizes the NetworkX library to analyze Zachary's Karate club graph. The graph represents the relationships between club members, with each member having an attribute called 'club' indicating the group they belong to after the separation of the club. The two groups are denoted as either "Mr. Hi" or "Officer."

## Program Features

1. **Printing Nodes and Edges**: The program prints out the list of nodes and edges, including their attributes.

2. **Visualization**: A visualization of the Karate club graph is provided, where the color of nodes represents the two groups after the separation.

3. **Shortest Path Calculation**: The program uses `nx.dijkstra_path()` to find the shortest path from node 24 to node 16. The resulting list of nodes along the path is printed.

4. **Highlighted Nodes Visualization**: Another visualization of the Karate club graph is provided, where the color of nodes along the shortest path is modified to highlight their selection. The selected nodes are shown in red.

## Usage
Install the required dependencies by running `pip install networkx`.



Feel free to explore and modify the program according to your needs.

Note: Make sure to have `matplotlib` installed for the visualizations to display properly.

## References

- [NetworkX Documentation](https://networkx.org/documentation/)
- [Zachary's Karate Club](https://en.wikipedia.org/wiki/Zachary%27s_karate_club)
