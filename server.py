from http import server
from os import error, pipe
import socket
import subprocess
import sys


#server types
SERV_DEFAULT = 100
SERV_LOGIN = 200

#commands
EXIT = '100'
LOGIN = '101'
LOGOUT = '102'

host = socket.gethostname()
port = 4000

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
except Exception as e:
    print("Failed to initialize server: "+str(e))

class Server():
    
    
    def server(self,login_p):
        while True:
            #check login server first
            out, err = login_p.communicate()
            if out:
                print(out)
            if err:
                print(err)
            #check for inputs from client
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8', 'strict')
            print("Message from " + str(addr) + ": " + data)
            if(data == EXIT):
                s.sendto("Server is shutting down.".encode('utf-8'), addr)
                self.close_server()
                break
            elif(data == LOGIN):
                self.login(addr)
            elif(data == '999'):
                print("test")
            else:
                s.sendto("Command does not exist.".encode('utf-8'), addr)
        s.close()


    def close_server():
        print("Shutting down server...")


    def wait_for_response(s):
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        return data


    def login(addr):
        s.sendto("Please provide your username.".encode('utf-8'), addr)
        print("waiting for username...")
        usrname, addr = s.recvfrom(1024)
        usrname = usrname.decode('utf-8', 'strict')
        if(usrname == 'guest'):
            s.sendto("Please provide your password".encode('utf-8'), addr)
            print("waiting for password...")
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8', 'strict')
            if(data == 'password'):
                print(str(usrname)+" logged in from "+str(addr) +".")
                msg = "Logged in as "+str(usrname)
                s.sendto(msg.encode('utf-8'), addr)
            else:
                print("Incorrect password login attempt for user " +str(usrname)+
                " from "+str(addr)+".")
                s.sendto("Incorrect password.".encode('utf-8'), addr)
        else:
            print("False username login attempt from "+str(addr)+" with username: "
            +str(usrname))
            msg = str(usrname)+" does not exist."
            s.sendto(msg.encode('utf-8'), addr)


    def login_server():
        print("Booting loginserver")
        try:
            login_p = subprocess.Popen([sys.executable, './login_server.py',
            '--username', 'root'], 
            stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
            return login_p
        except error as e:
            print("Failed to open login server:" + e)
            sys.exit()


    def initialize(server_type):
        print("Initializing server type: "+str(server_type))



if __name__ == '__main__':
    main_server = Server
    login_server = Server

    login_server.initialize(SERV_LOGIN)
    login_server.login(host)
    
    