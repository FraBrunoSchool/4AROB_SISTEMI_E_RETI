def iniPav(dim):
    pavimento = []
    # iniziallizzazione pavimento
    # le liste dentro a 'pavimento' sono le righe
    for r in range(0, dim):
        riga = []
        for c in range(0, dim): riga.append(True)
        pavimento.append(riga)
    return pavimento


def creaPav():
    # input dimensione n*n
    dim = int(input("Inserisci la dimensione del pavimento: "))
    return iniPav(dim)


def stampaPav(pav):
    for r in range(0, len(pav)):
        print(" ")
        for c in range(0, len(pav)): print(pav[r][c], end=' ')
    print(" ")


def creaNodi(pav):
    nNodi = 1
    for r in range(0, len(pav)):
        for c in range(0, len(pav)):
            if pav[r][c]:
                pav[r][c] = nNodi
                nNodi += 1


def createDic(pav):
    dict = {}
    x = 1  # spostamento dx, sx, su, giù
    nNodi = 1
    for r in range(0, len(pav)):
        for c in range(0, len(pav)):
            links = []
            if pav[r][c] != False:
                if r - x >= 0:
                    if (pav[r - x][c] != False): links.append(pav[r - x][c])
                if c - x >= 0:
                    if (pav[r][c - x] != False): links.append(pav[r][c - x])
                if c + x < len(pav):
                    if (pav[r][c + x] != False): links.append(pav[r][c + x])
                if r + x < len(pav):
                    if (pav[r + x][c] != False): links.append(pav[r + x][c])
                dict[nNodi] = links
                nNodi += 1
    return dict


def stampaDict(dict):
    print("\n{")
    for key, val in dict.items(): print(f"\t{key}: {val},")
    print("}")


def celleOccu(pav):
    while True:
        pos = input("Inserisci le cordinate della cella occupata (inserisci -1 per terminare) (prima riga e poi "
                    f"colonna da 1 a {len(pav)}): ")
        if pos != "-1": pav[int(pos.split(".")[0]) - 1][int(pos.split(".")[1]) - 1] = False
        else:
            if pos == "-1": break
    creaNodi(pav)
    return createDic(pav)


def main():
    p = creaPav()
    stampaPav(p)
    dict = celleOccu(p)
    stampaPav(p)
    stampaDict(dict)


if __name__ == '__main__':
    main()