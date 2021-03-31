import socket #importiamo il pacchetto socket

SERVER_ADDRESS = '127.0.0.1' #indirizzo server
SERVER_PORT = 22224 #porta server

sock_service = socket.socket() #crea la richiesta del servizio

sock_service.connect((SERVER_ADDRESS, SERVER_PORT)) #invia la richiesta del servizio e crea la richiesta

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT))) #comando per verificare che il collegamento sia in funzione
protocollo= ["SYN", "SYN ACK", "ACK with data", "ACK for data"]
dati = '0'
while True:
    print("Invio: " + dati + " - " + protocollo[int(dati)])
    dati = dati.encode() #vengono codificati i dati

    sock_service.send(dati) #vengono inviati i dati
    
    dati = sock_service.recv(2048) #aspetta la risposta dal server

    if not dati: #controllo risposta del server
        print("Server non risponde. Exit")
        break # se non risponde chiude il collegamento
    
    dati = dati.decode() # se risponde vengono decodificati i dati
    if dati=='3':
        print("Ricevuto: " + dati + " - " + protocollo[int(dati)])
        print("Termino connessione")
        break
    else:
        print("Ricevuto: " + dati + " - " + protocollo[int(dati)])
        dati=int(dati)+1
        dati=str(dati)


sock_service.close() #se l'utente inserisce 0 o se il server non risponde, si chiude la connessione
#print("Termino connessione")