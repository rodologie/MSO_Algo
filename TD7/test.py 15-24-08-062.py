# import networkx as nx
# import random
# import matplotlib.pyplot as plt

# def random_graph():
#     n = random.randint(7,10)
#     m = random.randint(round(1.3*n),round(1.7*n))

#     # Création du graphe aléatoire pondéré
#     G = nx.gnm_random_graph(n, m)
#     print(G.edges())

#     # Attribution de poids aléatoires aux arêtes
#     for (u, v) in G.edges():
#         G.edges[u, v]['weight'] = random.randint(1, 10)

#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True)
#     labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
#     return G

# plt.figure(1)
# G=random_graph()




# def kruskal(graph):
#     # Crée un arbre vide pour stocker les arêtes ajoutées
#     tree = nx.Graph()

#     # Trie toutes les arêtes du graphe en fonction de leur poids
#     lst = []
#     for edge in graph.edges(data=True):
#         lstnode = []
#         lsti=[]
#         node1 = edge[0]
#         node2 = edge[1]
#         weight = edge[2]['weight']
#         lstnode.append(node1)
#         lstnode.append(node2)
#         lsti.append(lstnode)
#         lsti.append(weight)
#         lst.append(lsti)
#     edges = sorted(lst, key = lambda x: x[1])



#     # Parcourt chaque arête du graphe trié
#     for edge in edges:
#         node1 = edge[0][0]
#         node2 = edge[0][1]
#         weight = edge[1]
#         print("node1: ", node1, "   |    node2: ", node2)
#         tree.add_edge(node1, node2, weight=weight)
#         try: 
#             nx.find_cycle(tree,node1)
#             tree.remove_edge(node1, node2)
#         except:
#             pass
            

#     return tree

# plt.figure(2)
# T = kruskal(G)
# nx.draw(T, pos=nx.spring_layout(T), with_labels=True)

# plt.show()


import folium
import osmnx as ox
import osmnx.folium as ox_folium


Lyon = folium.Map(location=[45.75, 4.85], zoom_start=1, tiles='openstreetmap')
G = ox.graph_from_place('Rhône, France', network_type='drive')
carte = ox_folium.plot_graph_folium(G, graph_map=Lyon, popup_attribute='name', fit_bounds=True)

Lmaison = 46.198932250319395 

lmaison =4.689597670997221

node_maison = ox.nearest_nodes(G,Lmaison,lmaison)
print("Node maison: ", node_maison)