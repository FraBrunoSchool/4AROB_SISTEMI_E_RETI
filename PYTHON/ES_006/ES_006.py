import random


def push(stack, element):
    stack.append(element)
    return stack


def pop(stack):
    return stack, stack.pop()


class carta(object):
    def __init__(self, seme, numero):
        self.seme = seme
        self.numero = numero

    def stampa(self):
        print(f"la carta ha seme {self.seme} con numero {self.numero}.")


def divido(stack):
    primaParte = []

    for x in range(0, random.randint(0, 51)):
        push(primaParte, x)


def main():
    c = carta("C", 5)
    c.stampa()
    #k = 0
    mazzo = []
    semi = ["C", "P", "D", "F"]
    primaParte = []
    secondaParte = []

    for i in range(1, 14):
        for s in semi:
            push(mazzo, carta(s, i))

    for i in mazzo:
        i.stampa()

    taglio = random.randint(0, 51)

    print("\n" + str(taglio) + "\n")

    #for i in mazzo:
    #    if k < taglio:
    #        push(primaParte, i)
    #    else:
    #        push(secondaParte, i)
    #    k += 1

    primaParte = mazzo[0:taglio]
    secondaParte = mazzo[taglio:]

    print("\nPrima parte\n")

    for i in primaParte:
        i.stampa()

    print("\nSeconda parte\n")

    for i in secondaParte:
        i.stampa()

    mazzo = secondaParte + primaParte

    print("\nMazzo coppato e rimesso insieme\n")

    for i in mazzo:
        i.stampa()


if __name__ == '__main__':
    main()
