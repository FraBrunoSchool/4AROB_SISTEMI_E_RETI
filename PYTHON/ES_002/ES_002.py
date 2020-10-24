def main():
    l = []
    parole_piu_lunghe = []
    cond = True

    while cond:
        l.append(input("Parola: "))

        r = input("Ancora? y/n: ")

        if r != "Y" and r != "y":
            cond = False

    print(l)

    lung = int(input("Lunghezza parola minima: "))

    for i in l:
        if len(i) >= lung:
            parole_piu_lunghe.append(i)

    print(parole_piu_lunghe)


if __name__ == '__main__':
    main()
