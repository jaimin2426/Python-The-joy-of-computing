import networkx as nx
import matplotlib.pyplot as plt

g = nx.complete_graph(10)

nx.draw(g)
plt.show()