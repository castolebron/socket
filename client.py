#!/usr/bin/env python3
#from -- import
import socket, sys, random, os, time
import threading, multiprocessing
#variables
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 15
def generate_requests (SERVER_ADDRESS, SERVER_PORT):#INIZIA  generate_requests
   
    start_time_thread = time.time()
    print("Client PID: {pid}, Process Name: {process_name}, Thread Name: {thread_name}"
            .format(pid = os.getpid(),
            process_name = multiprocessing.current_process().name,#nome del processo
            thread_name = threading.current_thread().name)#nome del thread
    )
    try:
        sock_service = socket.socket()#creazione  client socket
        sock_service.connect((SERVER_ADDRESS, SERVER_PORT))#connessione al server
        print("{thread_name} Connecting to the Server: {server_address}:{server_port}"#stampo le info del server
                .format(thread_name = threading.current_thread().name,
                server_address = SERVER_ADDRESS,
                server_port = SERVER_PORT)
        )
    except sock_service.error as socket_service_error:
        print("{thread_name} Errore-> Error: {socket_service_error}"#stampo il messaggio di errore
                .format(thread_name = threading.current_thread().name,#ottenego il nome del thread
                socket_service_error = socket_service_error)#inserire l'errore del servizio socket

        )
        print("\nExiting...")
        sys.exit()
    
    commands = ['piu', 'meno', 'per', 'diviso']
    operation = commands[random.randint(0,3)]
    data = str(operation) + ";" + str(random.randint(1,100)) + ";" + str(random.randint(1,100))
    data = data.encode()#encoding data
    sock_service.send(data)
    data = sock_service.recv(2048)
    if not data:
        print("{thread_name}: Server doesn't response. Exiting".format(thread_name = threading.current_thread().name))
   
    data = data.decode()#decoding 
    print("{thread_name} Received from the Server: " + data + "\n"
            .format(thread_name = threading.current_thread().name)
    )
    data = "E"#carattere per chiudere 
    data = data.encode()#encoding 
    sock_service.send(data)#mando la data 
    sock_service.close()
    end_time_thread = time.time()
    print("{thread_name} Execution time: {exe_time}"
            .format(thread_name = threading.current_thread().name,
            exe_time = end_time_thread - start_time_thread)
    )

if __name__ == '__main__':
    
    start_time = time.time()
    processes = [multiprocessing.Process(target = generate_requests, args = (SERVER_ADDRESS, SERVER_PORT))for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]  
    end_time = time.time()
    print("{process_name} Execution time: {exe_time}"
            .format(process_name = multiprocessing.current_process().name,
            exe_time = end_time - start_time)
    )
