import threading
import logging
from random import *

nBiglietti = 100
s = threading.Lock()


def cassa():
    global nBiglietti
    s.acquire()
    biglietti = randint(1, 10)
    logging.info(f"Sono il cliente {threading.get_ident()} e voglio acquistare {biglietti} biglietti")
    if nBiglietti == 0:
        logging.info("Biglietti finiti\n")
    elif nBiglietti > 0 and biglietti <= nBiglietti:
        logging.info(f"Biglietti acquistati {biglietti}\n")
        nBiglietti = nBiglietti - biglietti
    elif 0 < biglietti > nBiglietti:
        logging.info(f"Biglietti acquistati {nBiglietti}\n")
        nBiglietti = 0
    logging.info(f"Biglietti Disponibili {nBiglietti}\n")
    s.release()


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    c = [threading.Thread(target=cassa) for _ in range(0, 20)]
    for t in c: t.start()
    for t in c: t.join()

    logging.info("PADRE: procedura terminata")


if __name__ == "__main__":
    main()
