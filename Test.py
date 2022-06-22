from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt  # plotting
import numpy as np  # linear algebra
import os  # accessing directory structure
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import networkx as nx


class graphVisualization:

 def __init__(self):
  self.visual = []

 def addEdge(self, a, b):
  temp = [a, b]
  self.visual.append(temp)

 def visualize(self):
  G = nx.Graph()
  G.add_edges_from(self.visual)
  nx.draw_networkx(G)
  plt.show()


G = graphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()