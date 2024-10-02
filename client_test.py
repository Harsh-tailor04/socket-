# CLIENT

import socket

def start_client():
    server_ip = "377b-205-254-163-130.ngrok-free.app" # Ask for server IP
    port = 12345  # Must match the server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))  # Connect to the server

    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        client_socket.send(message.encode('utf-8'))  # Send message

    client_socket.close()  # Close the client socket

if __name__ == "__main__":
    start_client()