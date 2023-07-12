import socket
import threading
import json


def handle_client(connection_sock):
    current_user = None


    while True:
        encrypted_message = connection_sock.recv(1024)
        decrypted_message = encrypted_message

        command = decrypted_message.decode()
        command_dict = json.loads(command)
        print(f'Receiving: {connection_sock.recv(1024).decode()}')

        response = ''

        if command_dict['type'] == 'login':
            response, current_user = answer_login(command_dict['username'], command_dict['password'], current_user)
        

        print(f'Sending:\n{response}')
        connection_sock.send(response.encode())


def answer_login(username, password, current_user):
    if current_user is not None:
        message = {'type': 'ERROR', 'message': 'Exit Required'}
    else:
        for user in all_users['Users']:
            if user['username'] == username:
                if user['password'] == password:
                    message = {'type': 'OK', 'message': 'Login Successful'}
                    current_user = username
                    online_users.append(username)
                else:
                    message = {'type': 'ERROR', 'message': 'Password is not Correct'}
                break
        else:
            message = {'type': 'ERROR', 'message': 'Username not Found'}
    return json.dumps(message), current_user


HOST, PORT = 'localhost', 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
server_socket.bind(server_address)
server_socket.listen(1)

with open('Server/Users.txt', 'r') as file:
    all_users = json.loads(file.read())
online_users = []

print('Server Listening...')
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()