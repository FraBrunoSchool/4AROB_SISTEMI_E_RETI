import threading
import logging
import time


def fn_thread(val):
    logging.info(f"Thread {val}: inizio")
    time.sleep(2)
    logging.info(f"Thread {val}: fine")


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("PADRE : creo un thread")
    x = threading.Thread(target=fn_thread, args=(1,))
    logging.info("PADRE : avvio threa creato")
    x.start()
    logging.info("PADRE : aspetto terminazione del thread creato")
    x.join()
    logging.info("PADRE : fine")


if __name__ == '__main__':
    main()
