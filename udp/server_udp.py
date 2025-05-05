import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((host, port))
    print("Serveur UDP en écoute...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Reçu de {client_address} : {message}")
        
        if message.lower() == 'exit':
            print("Client a quitté.")
            break

        response = input("Répondre : ")
        server_socket.sendto(response.encode(), client_address)
