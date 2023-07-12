import socket


HOST, PORT = 'localhost', 8080
server_address = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

message = input('Enter your Message:\n')
print(f'Sending:\n{message}')
client_socket.send(message.encode())
response, _ = client_socket.recvfrom(1024)
print(response.decode())