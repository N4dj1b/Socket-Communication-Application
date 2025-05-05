import socket
import threading

host = '127.0.0.1'
port = 65432

def handle_client(conn, addr):
    print(f"Nouvelle connexion : {addr}")
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode()
                print(f"[{addr}] dit : {message}")
                response = f"Reçu : {message}"
                conn.sendall(response.encode())
            except ConnectionResetError:
                break
    print(f"Client {addr} déconnecté.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Serveur TCP multi-clients en écoute sur {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

# doesnt logout when all clients are disconnected