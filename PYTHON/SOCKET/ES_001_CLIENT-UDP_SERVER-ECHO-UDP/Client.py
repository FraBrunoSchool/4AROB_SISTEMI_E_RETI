import socket as sck


def client():
    # "192.168.88.96"

    server_ip = "192.168.88.107"
    server_port = 7000     # server port number

    c = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    # instantiate

    print("Enter 'exit' to end the connection")
    msg = input("->")   # take input

    while True:

        c.sendto(msg.encode(), (server_ip, server_port))    # send message

        data = c.recv(4096)    # receive message

        print(f"Received from server: {data.decode()}")   # show response

        msg = input("->")   # again take input

        if msg == "exit":
            c.sendto(msg.decode(), (server_ip, server_port))  # send message
            print("Close the connection")
            break

    c.close()   # close the connection


if __name__ == '__main__':
    client()
