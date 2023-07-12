import socket
import json


HOST, PORT = 'localhost', 8080
server_address = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    command = input('Enter your Message:\n')
    print(f'Sending:\n{command}')
    
    command = command.split(' ')
    if command[0] == 'signup' and len(command) == 3:
        message_to_send = json.dumps({'type': 'signup', 'username': command[1], 'password': command[2]})
    client_socket.send(message_to_send.encode())
    response, _ = client_socket.recvfrom(1024)
    print(f'Receiving:\n{response.decode()}')