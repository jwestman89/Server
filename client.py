# This implements the client side of a simple python server
import sys
from os import error
import socket

EXIT = '100'

host = socket.gethostname()
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def client():
    cmd = 'x'
    while cmd != EXIT:
        cmd = input("-> ")
        status = send_cmd(cmd)
        if(status == 'OK'):
            data = wait_for_response(s)
            if(data != 'NA'):
                print("Received from server: " + data)
    print("Exiting client.")
    s.close()


def send_cmd(cmd):
    try:
        s.sendto(cmd.encode('utf-8', 'strict'), (host, port))
        return 'OK'
    except Exception as e:
        print("Failed to send command: "+str(e))
        return 'NOK'


def wait_for_response(s):
    try:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
    except Exception as e:
        print("Server not responding: "+str(e))
        data = "NA"
    return data


def initialize():
    print("Initializing the client...")


def main():
    initialize()


if __name__ == "__main__":
    main()
    client()