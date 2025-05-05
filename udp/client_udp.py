import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    print("Client UDP prêt.")
    while True:
        message = input("Envoyer au serveur (ou 'exit' pour quitter) : ")
        client_socket.sendto(message.encode(), (host, port))
        
        if message.lower() == 'exit':
            print("Déconnexion...")
            break

        data, _ = client_socket.recvfrom(1024)
        print("Réponse du serveur :", data.decode())
