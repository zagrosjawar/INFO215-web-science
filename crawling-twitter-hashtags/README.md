# Hashtag Crawling and Graph Analysis

This program utilizes Selenium and NetworkX libraries to perform hashtag crawling and graph analysis. The details of the task are as follows:

## Task Description

1. Use Selenium to follow hashtag links.
2. Perform breadth-first search (BFS) in two steps:
   - Step 1: Crawl hashtags starting from a specific hashtag, for example, #Oslo.
   - Step 2: Crawl hashtags starting from another specific hashtag, for example, #Bergen.
3. Keep track of already visited hashtags and ensure that each hashtag is visited only once.
4. Follow a minimum of 20 hashtags in each step.
5. While visiting hashtag pages, add new connections in an undirected graph.
6. Implement error handling in the program.
7. Output the resulting graph in GraphML format.
8. Import the generated graph in Gephi as an undirected graph.
9. Adjust the size of the graph based on the degree of nodes.
10. Change the color of nodes based on modularity.
11. Fix the layout of the graph to enhance its presentation.

## Requirements

- Python 3.x
- Selenium
- NetworkX
- Matplotlib
- Gephi

## Usage

1. Install the required dependencies by running `pip install selenium networkx matplotlib`.

2. Download and install the latest version of the ChromeDriver from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system's PATH (the main directory/folder of your files).

3. Open the `main.py` file and update the following lines to set up the initial configuration:

```python
initial_hashtags = ["Bergen", "Oslo"]
```

4. Run the program using the following command:

```bash
python main.py
```

5. The program will perform hashtag crawling and generate two separate graphs for Bergen and Oslo.

6. The resulting graphs will be combined into a single graph.

7. The combined graph will be saved in GraphML format as `oslo_bergen_hashtags.graphml`.

8. Open Gephi and import the `oslo_bergen_hashtags.graphml` file to visualize and analyze the graph.

## Additional Notes

- The program uses Selenium with ChromeDriver to interact with Twitter's search functionality. Make sure to have Chrome installed on your system.

- The program implements BFS to crawl hashtags and create the graph. The BFS algorithm is used to explore nodes and edges of the graph.

- The resulting graph is saved in GraphML format, which can be easily imported into Gephi for further analysis and visualization.

- The size of the graph is adjusted based on the degree of nodes, and the color of nodes is determined by modularity.

- The layout of the graph is automatically adjusted by Gephi to enhance its presentation.

## References

- [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Gephi Documentation](https://gephi.org/users/)

(this description is chatGPT generated)

