import socket
import threading
import json

def handle_client(connection_sock):
    current_user = None
    while True:

        command = json.loads(connection_sock.recv(1024).decode())
        print(f'Receiving: {command}')
        if command['type'] == 'signup':
            response = answer_signup(command['username'], command['password'])
        elif command['type'] == 'login':
            response, current_user = answer_login(command['username'], command['password'], current_user)
        elif command['type'] == 'direct':
            response = answer_direct(command['contact'], command['message'], current_user)
        elif command['type'] == 'inbox':
            response = answer_inbox(current_user)
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


def answer_signup(username, password):
    for user in all_users['Users']:
        if user['username'] == username:
            message = {'type': 'ERROR', 'message': 'Username is used'}
            break
    else:
        all_users['Users'].append({'username': username, 'password': password})
        with open('Users.txt', 'w') as file:
            file.write(json.dumps(all_users, indent=4))
        message = {'type': 'OK', 'message': 'Signup Successful'}
    return json.dumps(message)


def answer_direct(contact, direct, current_user):
    for user in all_users['Users']:
        if user['username'] == contact:
            message = {'type': 'OK', 'message': 'Direct Message Delivered'}
            all_directs.append([current_user, contact, direct])
            break
    else:
        message = {'type': 'ERROR', 'message': 'Contact not found'}
    return json.dumps(message)


def answer_inbox(current_user):
    message = {'type': 'OK'}
    directs = []
    for direct in all_directs:
        if direct[1] == current_user:
            directs.append({'sender': direct[0], 'direct': direct[2]})
    message['directs'] = directs
    return json.dumps(message)


with open('Users.txt', 'r') as file:
    all_users = json.loads(file.read())

# each tuple: (sender, receiver, direct message)
all_directs = []

HOST, PORT = 'localhost', 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
server_socket.bind(server_address)
server_socket.listen(1)

with open('Users.txt', 'r') as file:
    all_users = json.loads(file.read())
online_users = []

print('Server Listening...')
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()