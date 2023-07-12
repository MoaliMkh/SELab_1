import socket
import threading


def handle_client(connection_sock):
    while True:
        print(f'Receiving: {connection_sock.recv(1024).decode()}')


HOST, PORT = 'localhost', 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
server_socket.bind(server_address)
server_socket.listen(1)

print('Server Listening...')
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
