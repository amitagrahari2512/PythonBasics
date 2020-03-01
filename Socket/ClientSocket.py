import socket

clientSocket = socket.socket()

clientSocket.connect(('localhost',9999))

name = input("Enter your name")

clientSocket.send(bytes(name,'utf-8'))

returnVal = clientSocket.recv(1024).decode()

print(returnVal)