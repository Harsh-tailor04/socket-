# SERVER

import socket

def start_server():
    host = '0.0.0.0'  # Listen on all interfaces
    port = 12345       # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for 1 connection

    print(f"Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()  # Accept a connection
    print(f"Connection from {addr} has been established!")

    while True:
        message = conn.recv(1024).decode('utf-8')  # Receive message
        if not message:
            break  # Break if no message is received
        print(f"Received: {message}")

    conn.close()  # Close the connection
    server_socket.close()  # Close the server socket

if __name__ == "__main__":
    start_server()