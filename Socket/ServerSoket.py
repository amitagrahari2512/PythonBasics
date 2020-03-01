import socket
print("Socket Two Types : Tcp,Udp")
print("Tcp = Connection Oriented")
print("Udp = Connection Less")

#Here we can pass TCP type of UDP type
#By Default it is TCP type
serverSocket = socket.socket()

#serverSocket run on this location
serverSocket.bind(('localhost',9999))

#Maximum 3 connection run at a time
serverSocket.listen(3)

print("Soket Created")
print("Waiting for connection")

while True:
    clientSocket, address = serverSocket.accept()
    name = clientSocket.recv(1024).decode()
    print("Connection Established with {} with address {} ".format(name, address))
    clientSocket.send(bytes("Welcome {} in Client Socket programming".format(name),'utf-8'))





