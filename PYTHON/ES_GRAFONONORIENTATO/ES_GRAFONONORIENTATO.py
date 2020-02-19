def main():
    V = int(input("Inserire il numero di nodi"))
    grafo = []
    for i in range(1, V + 1):
        E = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (usare la ',' come separatore): ").split(',')]
        colonna = []
        for dim in range(0, V):
            colonna.append(0)
        for j in E:
            if j != i:
                colonna[j - 1] = 1
        grafo.append(colonna)
    print(grafo)


if __name__ == '__main__':
    main()
