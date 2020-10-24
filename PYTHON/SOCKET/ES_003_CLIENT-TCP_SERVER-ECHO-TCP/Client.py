import socket as sck


def client():
    # get the server name
    host = "192.168.88.83"
    port = 7000  # server port number
    print("creo istanza")
    c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # instantiate
    print("connect")
    print("Enter 'exit' to end the connection")
    msg = input("->")  # take input

    while True:
        c.sendall(msg.encode())  # send message

        data = c.recv(1024).decode()  # receive response
        print(f"Received from server: {data}")  # show response

        msg = input("->")  # again take input

        if msg == "exit":
            c.sendall(msg.encode())  # send message
            print("Close the connection")
            break

    c.close()  # close the connection


if __name__ == '__main__':
    client()
