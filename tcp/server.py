import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    print("Serveur TCP en attente de connexion...")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connecté à {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Client déconnecté.")
                break
            message = data.decode()
            print(f"Client dit : {message}")
            
            response = input("Répondre : ")
            conn.sendall(response.encode())
