#!/usr/bin/env python3


input_string = 'Hello' 
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket  #importo la libreria sokcet 

SERVER_ADDRESS = '127.0.0.1'  #indirizzo server 
SERVER_PORT = 22224           #porta server 

sock_service = socket.socket()  #socket che crea la richiesta del serivizio 

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))  #socket che invia la richiesta del servizio  e creo la richiesta 

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))  #comando per verificare che  il collegamento  sia in funzione 
while True:
    try:
        dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ") #utente inserisce il numero di richieste 
    except EOFError:
        print("\nOkay. Exit")
        break
    if not dati:
        print("Non puoi inviare una stringa vuota!") #controllo che non sia stringa vuota 
        continue
    if dati == '0':  
        print("Chiudo la connessione con il server!") #quando utente inserisce 0 la connessione termina 
        break
    
    dati = dati.encode() #vengono decodificati i dati

    sock_service.send(dati)  #dati vengono inviati 

    dati = sock_service.recv(2048) #riceve la risposta dal server 

    if not dati:  #controllo che server mi risponda 
        print("Server non risponde. Exit")
        break  #altrimenti 
    
    dati = dati.decode() #i dati vengono decofificati 

    print("Ricevuto dal server:") #leggo i dati a schermo
    print(dati + '\n')

sock_service.close()
