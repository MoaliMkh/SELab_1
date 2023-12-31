import socket
import json

HOST, PORT = 'localhost', 8080
server_address = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:

    command = input('Enter your Message:\n').lower()
    command = command.split(' ')
    if command[0] == 'signup' and len(command) == 3:
        message_to_send = json.dumps({'type': 'signup', 'username': command[1], 'password': command[2]})
    elif command[0] == 'login' and len(command) == 3:
        message_to_send = json.dumps({'type': 'login', 'username': command[1], 'password': command[2]})
    elif command[0] == 'direct' and len(command) >= 3:
        message_to_send = json.dumps({'type': 'direct', 'contact': command[1], 'message': ' '.join(command[2:])})
    elif command[0] == 'inbox' and len(command) == 1:
        message_to_send = json.dumps({'type': 'inbox'})
    elif command[0] == 'online' and len(command) == 1:
        message_to_send = json.dumps({'type': 'online'})
    elif command[0] == 'new_group' and len(command) == 2:
        message_to_send = json.dumps({'type': 'new group', 'name': command[1]})
    elif command[0] == 'exit' and len(command) == 1:
        message_to_send = json.dumps({'type': 'exit'})
    else:
        print('Invalid Command')
        continue

    client_socket.send(message_to_send.encode())
    response, _ = client_socket.recvfrom(1024)
    print(f'Receiving: {response.decode()}')
