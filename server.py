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

    #system rights
    LOGGED_IN = False
    READ_RIGHTS = False
    WRITE_RIGHTS = False
    EXECUTE_RIGHTS = False

    #system variables
    SERVER_TYPE = 0

    def __init__(self, server_type):
        print("Initializing server type: "+str(server_type))
        self.SERVER_TYPE = server_type
        while True:
            #check login server first
            #out, err = login_p.communicate()
            #if out:
            #    print(out)
            #if err:
            #   print(err)
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
            elif(data == LOGOUT):
                self.logout(addr)
            else:
                print("Invalid command received")
                s.sendto("Command does not exist.".encode('utf-8'), addr)
        s.close()

    def initialize(self, server_type):
        pass


    def close_server(self):
        print("Shutting down server...")


    def wait_for_response(s):
        data, addr = s.recvfrom(1024)
        return data.decode('utf-8')


    def login(self,addr):
        s.sendto("Please provide your username.".encode('utf-8'), addr)
        print("waiting for username...", end=" ")
        usrname, addr = s.recvfrom(1024)
        usrname = usrname.decode('utf-8', 'strict')
        if(usrname == 'guest'):
            s.sendto("Please provide your password".encode('utf-8'), addr)
            print(" OK")
            print("waiting for password...", end=" ")
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8', 'strict')
            if(data == 'password'):
                self.LOGGED_IN = True
                self.READ_RIGHTS = True
                print(" OK")
                print(str(usrname)+" logged in from "+str(addr) +".")
                msg = "Logged in as "+str(usrname)
                s.sendto(msg.encode('utf-8'), addr)
            else:
                print(" FAIL")
                print("Incorrect password login attempt for user " +str(usrname)+
                " from "+str(addr)+".")
                s.sendto("Incorrect password.".encode('utf-8'), addr)
        else:
            print(" FAIL")
            print("False username login attempt from "+str(addr)+" with username: "
            +str(usrname))
            msg = str(usrname)+" does not exist."
            s.sendto(msg.encode('utf-8'), addr)

    def logout(self,addr):
        if(self.LOGGED_IN == True):
            self.LOGGED_IN = False
            self.READ_RIGHTS = False
            self.WRITE_RIGHTS = False
            self.EXECUTE_RIGHTS = False
            s.sendto("Logged out from server.".encode('utf-8'), addr)
            print("User logged out.")
        else:
            s.sendto("Not logged in.".encode('utf-8'), addr)


    def get_type(self):
        return self.SERVER_TYPE


    def get_userRights(self):
        return self.LOGGED_IN, self.READ_RIGHTS, self.WRITE_RIGHTS, self.EXECUTE_RIGHTS


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



if __name__ == '__main__':
    main_server = Server(SERV_DEFAULT)