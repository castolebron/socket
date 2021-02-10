#!/usr/bin/env python3


#input_string = 'Hello'
#print(type(input_string))
#input_bytes_encoded = input_string.encode()
#print(type(input_bytes_encoded))
#print(input_bytes_encoded)
#output_string=input_bytes_encoded.decode()
#print(type(output_string))
#print(output_string)

import socket
import sys

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

#La funzione riceve la socket connessa al server e la utilizza per richiedere il servizio
def invia_comandi(sock_service):
    while True:
        try: #try per evitare vari possibili errori
            dati = input("Inserisci i dati da inviare (ko per terminare la connessione): ")#inserimento dati in caso non trova errori
        except EOFError: #se c'è un errore
            print("\nOkay. Exit")# stampa questo 
            break #chiusura
        if not dati:# se non vengono insierriti dati 
            print("Non puoi inviare una stringa vuota!")# meaasggio
            continue# non chiude il ciclo ma lo continua comunque
        if dati == 'ko':#se viene inserito ko
            print("Chiudo la connessione con il server!")#il server si chiude
            break#chiusura
    
        dati = dati.encode() #.encode trasforma la stringa in byte
        sock_service.send(dati) #.send inivia a dati 
        dati = sock_service.recv(2048) #.recv riceve i dati

        if not dati:
            print("Server non risponde. Exit")
            break
        
        dati = dati.decode()

        print("Ricevuto dal server:")
        print(dati + '\n')
    sock_service.close()
        

#la funzionme crea una socket(s) per la connessione con il server e la passa alla funzione invia_comandi(s)
def connessione_server(address, port):
    sock_service = socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    invia_comandi(sock_service)
    

#Questo comando serve per far capire al codice se è stato eseguito come singolo script o se è stato chiamato come modulo da qualche altro
#programma per usare le sue funzioni o classi
if __name__ == '__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)