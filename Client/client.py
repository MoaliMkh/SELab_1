import socket
import json


HOST, PORT = 'localhost', 8080
server_address = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    command = input('Enter your Message:\n').lower()
    command_parts = command.split(' ')
    if command_parts[0] == 'login' and len(command_parts) == 3:
        message_to_send = {'type': 'login', 'username': command_parts[1], 'password': command_parts[2], }
        print(f'Sending:\n{json.dumps(message_to_send)}')
        client_socket.send(json.dumps(message_to_send).encode())
        response, _ = client_socket.recvfrom(1024)
        print(response.decode())

    else:
        print('Invalid Command')
        continue