import networkx as nx
import matplotlib.pyplot as plt


def main():
    v = int(input("Inserire il numero di nodi"))
    m = creaMatriceDaNumNodi(v)
    d = creaDictDaMatrice(m)
    stampaDict(d)
    m2 = creaMatriceDaDict(d, v)
    stampaMatrice(m2, v)
    drawGrafo(d)


def creaMatriceDaNumNodi(v):
    matrix = []
    for i in range(1, v + 1):
        e = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (usare la '.' come separatore): ").split('.')]
        colonna = [0 for dim in range(0, v)]
        for j in e:
            if j != i:
                colonna[j - 1] = int(input(f"Inserire il peso tra il nodo {i} e il nodo {j}"))
        matrix.append(colonna)

    return matrix


def creaDictDaNumNodi(v):
    dict = {}
    for r in range(0, v):
        chiave = r + 1
        edge = []
        occ = [int(i) for i in
               input(f"Inserire le vicinanze del nodo {chiave} (usare la '.' come separatore): ").split('.')]
        for j in occ:
            if j != occ:
                edge.append(int(input(f"Inserire il peso tra il nodo {chiave} e il nodo {j}")))
        dict[chiave] = {"neighbors": occ, "weights": edge}

    return dict


def creaDictDaMatrice(grafo):
    dict = {}
    for r in range(0, len(grafo)):
        chiave = r + 1
        occ = []
        edge = []
        for c in range(0, len(grafo)):
            if grafo[r][c] > 0:
                occ.append(c + 1)
                edge.append(grafo[r][c])
        dict[chiave] = {"neighbors": occ, "weights": edge}

    return dict


def creaMatriceDaDict(dict, v):
    matrix = []
    for key, val in dict.items():
        colonna = [0 for dim in range(0, v)]
        edge = val["neighbors"]
        peso = val["weights"]
        for e, p in zip(edge, peso):
            colonna[e - 1] = p
        matrix.append(colonna)

    return matrix


def stampaMatrice(matrix, v):
    for r in range(0, v):
        print(" ")
        for c in range(0, v):
            print(matrix[r][c], end=' ')


def stampaDict(dict):
    print("\n{")
    for key, val in dict.items():
        print(f"\t{key}: {val},")

    print("}")


def drawGrafo(dict):
    G = nx.Graph()
    for key, val in dict.items():
        G.add_node(key)
        edge = val["neighbors"]
        peso = val["weights"]
        for e, p in zip(edge, peso):
            G.add_edge(int(key), int(e), weight=p)
            G.edges[key, e]['weight']=p
    print(f"\n{nx.info(G)}")
    nx.draw(G)
    plt.show()


# FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])

if __name__ == '__main__':
    main()
