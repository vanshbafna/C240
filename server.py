import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None

clients = {}

def setup():
    print('\n \t\t\t IP Messenger\n')

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print('\n \t\t\t Server Is Waiting For Incoming Connections\n')
    acceptConnections()

def acceptConnections():
    global SERVER
    global clients

    while True:
        clients, addr = SERVER.accept()
        print(clients, addr)

setup_thread = Thread(target = setup)
setup_thread.start()    