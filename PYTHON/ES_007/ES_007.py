import subprocess


def convert_bin(address):
    ipaddress_bin = 0
    for e, group in enumerate(address):
        ipaddress_bin = ipaddress_bin + group * (2 ** (((3 - e) * 8)))

    return ipaddress_bin


def ping(address):
    # Scegliere il Sistema operativo commentando la riga del sistema operativo non in uso
    # windows
    # p = subprocess.Popen(['ping', address], stdout=subprocess.PIPE)
    # Linux
    p = subprocess.Popen(['ping', '-c 2', address], stdout=subprocess.PIPE)
    pingText = p.communicate()
    #print(pingText[0].decode())
    if pingText[0].decode().count('100% packet loss') == 1:
        print(f"L'host {address} non è attivo")
    else:
        if pingText[0].decode().count('100% packet loss') == 0:
            print(f"L'host {address} è attivo")


def address_list(address, mask):
    for c in range(1, 2 ** (32 - mask) - 1):
        address = address + 1
        l = '.'.join([str(int(bin(address)[i:i + 8], 2)) for i in range(2, 34, 8)])
        #print(l)
        ping(l)


def main():
    ipaddress = input("Inserisci un indirizzo IP: ")
    mask = int(input("Inserisci una maschera: "))

    ipaddress_splitted = [int(i) for i in ipaddress.split(".")]
    ipaddress_host = convert_bin(ipaddress_splitted)
    address_list(ipaddress_host, mask)


if __name__ == '__main__':
    main()
