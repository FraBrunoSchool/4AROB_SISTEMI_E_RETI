def push(stack, element):
    stack.append(element)
    return stack


def pop(stack):
    return stack, stack.pop()


def main():
    pila = [1, 2, 3, "ciao"]
    pila = push(pila, 5)
    print(pila)
    pila, _ = pop(pila)
    print(pila)
    #print(_)


if __name__ == '__main__':
    main()