#!/usr/bin/env python3
#from -- import
import socket
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_listen = socket.socket()

def socket_listen(sock_listen, SERVER_ADDRESS, SERVER_PORT):#parte il  socket_listen
    
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_listen.listen(5)
    print("Il server ascolta su: " + str((SERVER_ADDRESS, SERVER_PORT)))

def connected (addr_client):#parte la connessione
    
    print("\nConnesione ricevuta da " + str(addr_client))#stampo
    print("\nCreazione di thread per gestire le richieste")
    print("In attesa di ricevere dati ")

def operation (sock_service, addr_client):
   
    while True:#iniza il  while
        data = sock_service.recv(2048)
        if not data:
            print("fine data client.")
            break
        
        data = data.decode()
        print("\nRicevuto da " +  str(addr_client) + ": '%s'" %data)
        if data=='0':
            print("Chiusura connessione con : " + str(addr_client))
            break
        #end if
        separator = data.split(';')
        if separator[0] == "piu":
            ris = (float(separator[1]) + float(separator[2]))
        #end if
        if separator[0] == "meno":
            ris = (float(separator[1]) - float(separator[2]))
        #end if
        if separator[0] == "per":
            ris = (float(separator[1]) * float(separator[2]))
        #end if
        if separator[0] == "diviso":
            if separator[2] == '0':
                ris = str(separator[1]) + " / " + str(separator[2]) +  "non è possibile"
                data = "Risponde a : " + str(addr_client) + ".\n" + str(ris)
            else:
                ris = (float(separator[1]) / float(separator[2]))
            
       
        data = "Rispondi a : " + str(addr_client) + ".\n il risulato tra  " + str(separator[1]) + " e " + str(separator[2]) + " con " + str(separator[0]) + " e: " + str(ris)
        data = data.encode()
        sock_service.send(data)
    

def receiving_connections(sock_listen):
    
    socket_listen(sock_listen, SERVER_ADDRESS, SERVER_PORT)
    while True:#inizi il  while
        sock_service, addr_client = sock_listen.accept()
        connected(addr_client)
        try:
            Thread(target = operation, args = (sock_service, addr_client)).start()
        except:
            print("The thread doesn't run")
            sock_service.close()
 

receiving_connections(sock_listen)