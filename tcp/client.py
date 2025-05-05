import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))
    print("Connecté au serveur.")
    
    while True:
        message = input("Envoyer au serveur (ou taper 'exit') : ")
        if message.lower() == 'exit':
            print("Déconnexion...")
            break
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print("Réponse du serveur :", data.decode())
