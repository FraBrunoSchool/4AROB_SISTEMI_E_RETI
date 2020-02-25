import networkx as nx
import matplotlib.pyplot as plt


def main():
    v = int(input("Inserire il numero di nodi"))
    dict = creaDictDaNumNodi(v)
    stampaDict(dict)
    stampaMatrice(creaMatriceDaDict(dict, v), v)


def creaMatriceDaNumNodi(v):
    matrix = []
    for i in range(1, v + 1):
        e = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (usare la '.' come separatore): ").split('.')]
        colonna = [0 for dim in range(0, v)]
        for j in e:
            if j != i:
                colonna[j - 1] = 1
        matrix.append(colonna)

    return matrix


def creaDictDaNumNodi(v):
    dict = {}
    for r in range(0, v):
        chiave = r + 1
        occ = [int(i) for i in
               input(f"Inserire le vicinanze del nodo {chiave} (usare la '.' come separatore): ").split('.')]
        dict[chiave] = occ

    return dict


def creaDictDaMatrice(grafo):
    dict = {}
    for r in range(0, len(grafo)):
        chiave = r + 1
        occ = []
        for c in range(0, len(grafo)):
            if grafo[r][c] == 1:
                occ.append(c + 1)
        dict[chiave] = occ

    return dict


def creaMatriceDaDict(dict, v):
    matrix = []
    for key, val in dict.items():
        colonna = [0 for dim in range(0, v)]
        for link in val:
            colonna[link - 1] = 1
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
    G = nx.petersen_graph()
    listaNodi = []
    listaToupleLink = []
    for key, val in dict.items():
        listaNodi.append(key)
        for i in val:
            toupleLink = [int(key), int(i)]
            listaToupleLink.append(tuple(toupleLink))

    G.add_nodes_from(listaNodi)
    G.add_nodes_from(listaToupleLink)
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')



if __name__ == '__main__':
    main()
