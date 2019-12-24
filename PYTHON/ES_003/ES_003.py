def main():
    l1 = ["ciao", "best", "gianlu"]
    l2 = ["ciao", "bello", "ggg", " best"]
    l_uni = []

    for i in l1:
        if i in l2:
            l_uni.append(i)

    print(str(l1) + " - " + str(l2) + " - " + str(l_uni))


if __name__ == '__main__':
    main()
