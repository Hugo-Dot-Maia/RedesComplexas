from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt  # plotting
import numpy as np  # linear algebra
import os  # accessing directory structure
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import networkx as nx
import GraficoAmigos
import Alcance
import FeixoTransitivo
import MenorCaminho
import ProximaAmizade

G = nx.DiGraph()
nodes = np.arange(0, 15).tolist()
G.add_nodes_from(nodes)
G.add_edges_from([(0, 2), (0, 3), (0, 12), (0, 8), (0, 6),
                  (1, 2), (1, 13), (1, 0), (1, 11), (1, 8), (1, 6),
                  (2, 4), (2, 3), (2, 0), (2, 6),
                  (3, 13), (3, 12), (3, 8), (3, 0),
                  (4, 0), (4, 2),
                  (5, 9), (5, 14),
                  (6, 1), (6, 0), (6, 3), (6, 11),
                  (7, 12),
                  (8, 6), (8, 1), (8, 0), (8, 3), (8, 11), (8, 12),
                  (9, 12), (9, 14), (9, 15),
                  (10, 4), (10, 13),
                  (11, 8), (11, 6), (11, 1), (11, 0), (11, 13),
                  (12, 15), (12, 7), (12, 11), (12, 3),
                  (13, 10), (13, 2), (13, 12),
                  (14, 9),
                  (15, 12), (15, 14), (15, 5), (15, 9)
                  ])
labels = {0: "Agnese",
          1: "Alessandra", 2: "Chiara",
          3: "Elisa", 4: "Elvis",
          5: "Emanuele", 6: "Gabriella", 7: "Gianluca",
          8: "Giuliana", 9: "Lorenzo", 10: "Ludovica", 11: "Martina",
          12: "Matteo", 13: "Nicoletta", 14: "Pierfrancesco", 15: "Simone"}

nx.draw_networkx(G, labels=labels, arrows=True,
                 node_shape="s", node_size=1200,
                 node_color="white",
                 )

Alcance.confereAlcance()
FeixoTransitivo.transitive_closure()
menorCaminhoPorCrianca = MenorCaminho.menorCaminho(14)

amizade = ProximaAmizade.poximoAmigo(menorCaminhoPorCrianca, 14)
print("Próxima amizade é " + labels[amizade])

plt.title("Grafo das amizades da escola Elisa")
plt.show()
