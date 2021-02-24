import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_service = socket.socket()

def socket_connect (sock_service, SERVER_ADDRESS, SERVER_PORT):
  
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connessione a: " + str((SERVER_ADDRESS, SERVER_PORT)))

def input_data():

    while True:
        try:
            data = input("Inserisci operatore, numero uno e numero due da mandare: ")
        except EOFError:
            print("\nOkay. Esci")
            break
        if not data:
            print("non puoi inviare una stringa vuota!")
            continue
        
        if data == 'E' or data == 'e':
            print("connessione col server conclusa!")
            break
        
        data = data.encode()
        sock_service.send(data)
        data = sock_service.recv(2048)
        if not data:
            print("Il server non risponde")
            break
        
        data = data.decode()
        print("Ricevuto dal server:")
        print(data + '\n')
   
socket_connect(sock_service, SERVER_ADDRESS, SERVER_PORT)
input_data()
sock_service.close()