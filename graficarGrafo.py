# -*- coding: utf-8 -*-

from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt


"""
======================================================================================
    Grafo de entrada o Matriz de Adyacencia
======================================================================================
"""
# grafo = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['B', 'F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# grafo = {
#     'A': ['B', 'C', 'F'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D', 'E'],
#     'D': ['B', 'C', 'F'],
#     'E': ['C', 'F'],
#     'F': ['A', 'D', 'E']
# }

# grafo = {
#     'A': ['B', 'C', 'E'],
#     'B': ['A', 'C', 'D'],
#     'C': ['D'],
#     'D': ['C'],
#     'E': ['F', 'D'],
#     'F': ['C']
# }

grafo = {
    'S': ['2', '3'],
    '2': ['5', '6'],
    '3': ['9', '10'],
    '5': ['10', '15'],
    '6': ['12', '18'],
    '9': [],
    '10': [],
    '15': [],
    '12': [],
    '18': [],
    '10': []
}

# grafo = {
#     '1' : ['2','3','5'],
#     '2' : ['4'],
#     '3' : ['6'],
#     '4' : ['8'],
#     '5' : ['6'],
#     '6' : ['7','9'],
#     '7' : [],
#     '8' : [],
#     '9' : []
# }


"""
======================================================================================
    Aquí se define el Nodo Inicial y el Nodo Final o Nodo Buscado
======================================================================================
"""
inicio = 'S'
fin = "9"


"""
======================================================================================
    Inicialización de Variables para BFS
======================================================================================
"""
G_BFS = nx.Graph(grafo)
visitadoBFS = {}
distanciaBFS = {}
parentBFS = {}
recorridoBFS = []
queue = Queue()
caminoCorto = []

for nodo in grafo.keys():
    visitadoBFS[nodo] = False
    parentBFS[nodo] = None
    distanciaBFS[nodo] = -1


"""
======================================================================================
    Función BFS
======================================================================================
"""


def bfs(grafo, nodo, fin):
    global G_BFS
    visitadoBFS[nodo] = True
    distanciaBFS[nodo] = 0
    queue.put(nodo)

    while not queue.empty():
        nodo = queue.get()
        recorridoBFS.append(nodo)

        for n in grafo[nodo]:
            if not visitadoBFS[n]:
                visitadoBFS[n] = True
                parentBFS[n] = nodo
                print(nodo, n)
                distanciaBFS[n] = distanciaBFS[nodo]+1
                # Descomentar solo si se desea colocar pesos a la arista
                # G_BFS.add_edge(n, nodo, weight=distanciaBFS[n])
                queue.put(n)

    while fin is not None:
        caminoCorto.append(fin)
        fin = parentBFS[fin]
    caminoCorto.reverse()


"""
======================================================================================
    Inicialización de Variables para DFS
======================================================================================
"""
G_DFS = nx.Graph(grafo)
# W: White -> no visitado y no explorado
# G: Green -> visitado y no explorado
# B: Black -> visitado y explorado
visitadoDFS = set()
distanciaDFS = {}
parentDFS = {}
recorridoDFS = []
color = {}
tiempo = 0
counter = -1

# Tiempo de visita [Inicio, Fin]
tiempoVisita = {}

for nodo in grafo.keys():
    color[nodo] = "W"
    parentDFS[nodo] = None
    tiempoVisita[nodo] = [-1, -1]


"""
======================================================================================
    Función DFS
======================================================================================
"""


def dfs(visitadoDFS, grafo, nodo):
    global counter
    if nodo not in visitadoDFS:
        counter += 1
        distanciaDFS[nodo] = counter
        visitadoDFS.add(nodo)
        for neighbour in grafo[nodo]:
            dfs(visitadoDFS, grafo, neighbour)


def auxiliarDFS(nodo):
    global G_DFS
    global tiempo
    color[nodo] = "G"
    tiempoVisita[nodo][0] = tiempo
    recorridoDFS.append(nodo)
    tiempo += 1
    for n in grafo[nodo]:
        if color[n] == "W":
            parentDFS[n] = nodo
            # Descomentar solo si se desea colocar pesos a la arista
            # G_DFS.add_edge(nodo, n, weight=tiempo)
            auxiliarDFS(n)
    color[nodo] = "B"
    tiempoVisita[nodo][1] = tiempo
    tiempo += 1


"""
======================================================================================
    Resultados BFS
======================================================================================
"""
bfs(grafo, inicio, fin)

print("\nRecorrido BFS")
print("Parents\n", parentBFS)
print("Distancia\n", distanciaBFS)
print("Recorrido\n", caminoCorto)


"""
======================================================================================
    Resultados DFS
======================================================================================
"""
dfs(visitadoDFS, grafo, inicio)
auxiliarDFS(inicio)

print("\nRecorrido DFS")
print("Parents\n", parentDFS)
print("Distancia\n", distanciaDFS, "\n", tiempoVisita)
print("Recorrido\n", recorridoDFS)


"""
======================================================================================
    Función para graficar BFS
======================================================================================
"""
pos = nx.fruchterman_reingold_layout(G_BFS)
nx.draw_networkx_nodes(G_BFS, pos, node_size=500, label='')
nx.draw_networkx_edges(G_BFS, pos, edgelist=G_BFS.edges(), edge_color='black')
nx.draw_networkx_labels(G_BFS, pos)
edge_labels = nx.get_edge_attributes(G_BFS, "weight")
nx.draw_networkx_edge_labels(G_BFS, pos, edge_labels)

for key, values in pos.items():
    # print("Key:", key, values[0], values[1])
    if distanciaBFS[key] == -1:
        plt.text(values[0]+0.05, values[1]+0.1, "Inalcanzable")
    else:
        plt.text(values[0]+0.05, values[1]+0.1, distanciaBFS[key])

plt.title("BFS: Breadth First Search")
plt.axis("off")
plt.show()


"""
======================================================================================
    Función para graficar DFS
======================================================================================
"""
pos = nx.fruchterman_reingold_layout(G_DFS)
nx.draw_networkx_nodes(G_DFS, pos, node_size=500, label='')
nx.draw_networkx_edges(
    G_DFS, pos, edgelist=G_DFS.edges(), edge_color='black')
nx.draw_networkx_labels(G_DFS, pos)
edge_labels = nx.get_edge_attributes(G_DFS, "weight")
nx.draw_networkx_edge_labels(G_DFS, pos, edge_labels)

for key, values in pos.items():
    # print("Key:", key, values[0], values[1])
    if key not in distanciaDFS:
        plt.text(values[0]+0.05, values[1]+0.1, "Inalcanzable")
        # plt.text(values[0]+0.05, values[1]+0.1, tiempoVisita[key])
    else:
        plt.text(values[0]+0.05, values[1]+0.1, distanciaDFS[key])
        # plt.text(values[0]+0.05, values[1]+0.1, tiempoVisita[key])

plt.title("DFS: Depth First Search")
plt.axis("off")
plt.show()
