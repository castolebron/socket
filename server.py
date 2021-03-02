#!/usr/bin/env python3
#from -- import
import socket
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_listen = socket.socket()

def socket_listen(sock_listen, SERVER_ADDRESS, SERVER_PORT):
    
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_listen.listen(5)
    print("Server listening on: %s" % str((SERVER_ADDRESS, SERVER_PORT)))#stampo informazioni server 

def connected (addr_client):#inizia la connessione
    
    print("\nConnection received from " + str(addr_client))
    print("\nCreating threads for manage the requests")
    print("Waiting for receive data ")

def operation (sock_service, addr_client):
    
    while True:
        data = sock_service.recv(2048)
        data = data.decode()
        if not data:
            print("End data client. Reset")
            break
        elif data == "E":
            print("Exiting...")
            break
       
        print("\nReceived from " +  str(addr_client) + ": '%s'" %data)
        if data=='0':
            print("Closing connection with: " + str(addr_client))
            break
        #comincia la calcolatrice
        separator = data.split(';')
        if separator[0] == "piu":
            ris = (float(separator[1]) + float(separator[2]))
       
        if separator[0] == "meno":
            ris = (float(separator[1]) - float(separator[2]))
        
        if separator[0] == "per":
            ris = (float(separator[1]) * float(separator[2]))
        
        if separator[0] == "diviso":
            if separator[2] == '0':
                ris = str(separator[1]) + " / " + str(separator[2]) +  " is not possible"
                data = "Answer to: " + str(addr_client) + ".\n" + str(ris)
            else:
                ris = (float(separator[1]) / float(separator[2]))
            
        
        data = "Answer to: " + str(addr_client) + ".\n The result between " + str(separator[1]) + " and " + str(separator[2]) + " with the " + str(separator[0]) + " is: " + str(ris)
        data = data.encode()
        sock_service.send(data)
    
    sock_service.close()

def receiving_connections(sock_listen):
    
    socket_listen(sock_listen, SERVER_ADDRESS, SERVER_PORT)
    while True:
        sock_service, addr_client = sock_listen.accept()
        connected(addr_client)
        try:
            Thread(target = operation, args = (sock_service, addr_client)).start()#creazione thread
        except:
            print("The thread doesn't run")
            sock_service.close()
    

receiving_connections(sock_listen)