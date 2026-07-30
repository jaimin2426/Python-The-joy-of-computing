import networkx as nx
import matplotlib.pyplot as plt

g = nx.barabasi_albert_graph(50,2)

nx.draw(g)
plt.show()

nx.write_gexf(g,"analysi1.gexf")