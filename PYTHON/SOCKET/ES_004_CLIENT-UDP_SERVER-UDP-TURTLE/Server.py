import socket as sck
import turtle


def server():

    # get the hostname
    host = "127.0.0.1"
    port = 6000     # initiate port

    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    # get instance

    s.bind((host, port))    # bind host address and port

    listaTurtle = []

    while True:

        data, address = s.recvfrom(4096)    # receive message
        if address not in listaTurtle:
            listaTurtle.append(address)
            listaTurtle.append(turtle.Turtle())

        if address in listaTurtle:
            istruction(data, listaTurtle[listaTurtle.index(address)+1])


        if not data.decode() or data.decode() == "exit":
            # if data is not received or data is the word 'exit' to end the connection break
            print("Close the connection")
            break

        #s.sendto("Prossimo".encode(), address)    # send data to the client

    s.close()    # close the connection


def istruction(istr, t):
    istr = istr.decode()
    command = istr.split("_")[0]
    number = int(istr.split("_")[1])
    if command == "a":
        t.fd(number)
    if command == "i":
        t.bk(number)
    if command == "d":
        t.right(number)
    if command == "s":
        t.left(number)

    turtle.done()



if __name__ == '__main__':
    server()
