import socket
import threading
import json


def handle_client(connection_sock):
    while True:
        command = json.loads(connection_sock.recv(1024).decode())
        print(f'Receiving: {command}')
        if command['type'] == 'signup':
            response = answer_signup(command['username'], command['password'])


def answer_signup(username, password):
    for user in all_users['Users']:
        if user['username'] == username:
            message = {'type': 'ERROR', 'message': 'Username is used'}
            break
    else:
        all_users['Users'].append({'username': username, 'password': password})
        with open('Server/Users.txt', 'w') as file:
            file.write(json.dumps(all_users, indent=4))
        message = {'type': 'OK', 'message': 'Signup Successful'}
    return json.dumps(message)


with open('Server/Users.txt', 'r') as file:
    all_users = json.loads(file.read())

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
