#This is a subprocess of the Server program.
import time
import socket

EXIT = '100'
LOGIN = '101'
LOGOUT = '102'

LOGGED_IN = False
READ_RIGHTS = False
WRITE_RIGHTS = False
EXECUTE_RIGHTS = False

host = socket.gethostname()
port = 4001

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
except Exception as e:
    print("Failed to initialize login server: "+str(e))



def login():
    print("login")


def initialize():
    msg = "Initializing login server"


if __name__ == '__main__':
    initialize()
    