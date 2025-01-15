import matplotlib.pyplot as plt
import networkx as nx
import random

# Graph Creation
def GraphGenerator(nodes):
    
    G = nx.Graph()
    for alpha in nodes:
        G.add_node(chr(alpha))

    # Edges
    for alpha in nodes:
        for beta in nodes:
            if(alpha >= beta):
                continue

            add_prob = random.randint(0, 1)
            if add_prob == 1:
                print("adding edge for", alpha, " ", beta)
                G.add_edge(chr(alpha), chr(beta))
    return G


# Drawing & Plotting
def DrawGraph(G):
    nx.draw(G, with_labels=True, node_color="brown", node_size=2000, font_color="white", font_size=20, width=5)
    plt.margins(0.2)
    plt.show()

nodes = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
G=GraphGenerator(nodes)
DrawGraph(G)
