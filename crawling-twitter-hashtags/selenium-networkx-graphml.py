import networkx as nx
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


op = Options()
op.add_argument("--no-headless")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=op, service=s)


# Load the initial hashtag (#Oslo and #Bergen) and set as current node.
# Create node in your nx-graph.

def scrolldown():
    for i in range(30):
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(.3)

def login():
    driver.get("https://twitter.com/hashtag/Test")
    time.sleep(40)

def graph_hashtags(graph, hashtag_name):
    visited = []
    todo = [hashtag_name]
    login()
    while len(visited) <= 20 and todo:
        current_hashtag = todo.pop(0)
        visited.append(current_hashtag)

        driver.get("https://twitter.com/search?q=%23" + current_hashtag)
        try:
            element_present = EC.presence_of_element_located((By.XPATH,
                                                            "//*[@class='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu']"))
            WebDriverWait(driver, 20).until(element_present)

            # scrolldown()

        except TimeoutException:
            print("Timed out waiting for page to load")

        hashtags = driver.find_elements(By.XPATH, "//a[contains(@href, '/hashtag/')]")

        for hashtag in hashtags:
            # hashtag_link = hashtag.get_attribute("href")
            hashtag_text = hashtag.text
            hashtag_name = hashtag_text.strip("#")
            if not hashtag_name:  # to skip the empty hashtags after stripping "#"
                continue
            # print(hashtag_link)
            # print(hashtag_name)
            if hashtag_name not in visited and hashtag_name not in todo:
                todo.append(hashtag_name)

        for hashtag in todo:
            if hashtag != current_hashtag:
                graph.add_edge(current_hashtag, hashtag)


# BFS Search Algorithm
# Used to explore nodes and edges of a graph.

def bfs(graph, start_node):
    # queue for BFS traversing
    # set to keep track of visited nodes
    visited = {start_node}
    queue = [start_node]

    # bfs graph
    bfs_graph = nx.Graph()
    while queue:
        # dequeue and constructing the bfs graph.
        current_node = queue.pop(0)
        bfs_graph.add_node(current_node)
        neighbors = graph.neighbors(current_node)
        # print(current_node)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

                bfs_graph.add_edge(current_node, neighbor)
    return bfs_graph


# Bergen and Oslo Graphs
G_Bergen = nx.Graph()
G_Oslo = nx.Graph()
initial_hashtags = ["Bergen", "Oslo"]
graphs = [G_Bergen, G_Oslo]
for i in range(len(graphs)):
    graph_hashtags(graphs[i], initial_hashtags[i])


G1 = bfs(G_Bergen, "Bergen")
G2 = bfs(G_Oslo, "Oslo")

combined_graph = nx.compose(G1, G2)
# print(combined_graph.nodes())
nx.write_graphml(combined_graph, "oslo_bergen_hashtags.graphml")

