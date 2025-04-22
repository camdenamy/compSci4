import networkx as nx
import matplotlib.pyplot as plt

# Create a MultiGraph (allows multiple edges between nodes)
G = nx.MultiGraph()

# Define nodes (land masses)
G.add_nodes_from(["A", "B", "C", "D"])

# Define edges (bridges)
G.add_edge("A", "C")  # Bridge 1
G.add_edge("A", "C")  # Bridge 2
G.add_edge("A", "D")  # Bridge 3
G.add_edge("B", "C")  # Bridge 4
G.add_edge("B", "C")  # Bridge 5
G.add_edge("B", "D")  # Bridge 6
G.add_edge("C", "D")  # Bridge 7

# Display node degrees
print("Degrees of each node:")
for node in G.nodes:
    print(f"{node}: {G.degree(node)}")

# Draw the graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_weight='bold')
plt.title("Seven Bridges of Königsberg (Graph Representation)")
plt.show()