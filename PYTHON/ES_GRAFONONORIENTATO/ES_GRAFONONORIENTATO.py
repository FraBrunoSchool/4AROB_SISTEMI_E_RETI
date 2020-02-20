def main():
    v = int(input("Inserire il numero di nodi"))
    grafo = creaMatrice(v)
    stampaMatrice(grafo, v)
    dict = adj2dict(grafo)
    print(dict)


def creaMatrice(v):
    grafo = []
    for i in range(1, v + 1):
        e = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (usare la ',' come separatore): ").split(',')]
        colonna = [0 for dim in range(0, v)]
        for j in e:
            if j != i:
                colonna[j - 1] = 1
        grafo.append(colonna)

    return grafo


def adj2dict(grafo):
    dict = {}
    for r in range(0, len(grafo)):
        chiave = r + 1
        occ = []
        for c in range(0, len(grafo)):
            if grafo[r][c] == 1:
                occ.append(c+1)
        dict[chiave] = occ

    return dict


def stampaMatrice(grafo, v):
    for r in range(0, v):
        print(" ")
        for c in range(0, v):
            print(grafo[r][c], end=' ')


if __name__ == '__main__':
    main()

"""
dizionario delle adiacenze
"""
