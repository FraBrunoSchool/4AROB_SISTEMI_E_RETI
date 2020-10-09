def main():
    l = []

    for i in range(int(input("Dimensione lista: "))):
        l.append(input("Numero: "))

    print(l)
    l.sort()
    print(l)

if __name__ == '__main__':
    main()