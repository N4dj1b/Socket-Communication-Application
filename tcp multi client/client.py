import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))
    print("Connecté au serveur.")
    
    while True:
        message = input("Message (ou 'exit' pour quitter) : ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024)
        print("Serveur :", response.decode())
