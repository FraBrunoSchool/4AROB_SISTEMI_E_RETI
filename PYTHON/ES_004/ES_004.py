import random as rnd

def main():
    nameList = ["Nardi", "Bernardi", "Badoino"]

    for num, student in enumerate(nameList):
        print(f"{num} - {student}")

    print(f"Viene interrogato: {nameList[rnd.randint(0, len(nameList) - 1)]}")


if __name__ == '__main__':
    main()
