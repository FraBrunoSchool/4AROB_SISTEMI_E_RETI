def main():
    """"
    print("ciao")
    x = 123456789
    print(f"x vale: {x}")
    for i in range(0, 10):
        if i % 2 == 0:
            print(f"Il valore è {i} è pari")
        else:
            print(f"Il valore è {i} è dispari")
    """

    lista = [1, "ciao", 3, somma(3, 9)]
    for i in lista:
        print(i)


def somma(a, b):
    return a+b


if __name__ == '__main__':
    main()
