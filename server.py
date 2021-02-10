#!/usr/bin/env python3
import socket


#è indifferente riempire questo campo o no
SERVER_ADDRESS = '127.0.0.1'
#numero porta, obbligatoriamente > 1024 perché le altre sono private
SERVER_PORT = 22224

def ricevi_comandi(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nAspetto di ricevere i dati ")
        contConn=0
        while True:
            dati = sock_service.recv(2048)
            contConn+=1
            if not dati:#se non riceve dati chiude la connessione
                print("Fine dati dal client. Reset")
                break
            
            dati = dati.decode()
            print("Ricevuto: '%s'" % dati)
            if dati=='ko':#se riceve ko chiude la connessione
                print("Chiudo la connessione con " + str(addr_client))
                break
            operazione, primo, secondo = dati.split(";")#.split
            #Vari if per selezionare l'operazione che il client ha inserito
            if operazione == "piu":
                risultato = int(primo) + int(secondo)
            if operazione == "meno":
                risultato = int(primo) - int(secondo)
            if operazione == "per":
                risultato = int(primo) * int(secondo)
            if operazione == "diviso":
                risultato = int(primo) / int(secondo)
            
            dati = "Il risultato dell'operazione: "+operazione +" tra "+primo+" e "+secondo+" è: "+str(risultato)#output
            dati = dati.encode()
            sock_service.send(dati)
        sock_service.close()

def avvia_server(address, port):
    sock_listen = socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((address, port))
    sock_listen.listen(5)#consente un massimo di 5 client in coda
    print("Server in ascolto su %s." % str((address, port)))
    ricevi_comandi(sock_listen)

if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)