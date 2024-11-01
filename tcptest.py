import socket

x = socket.socket()
x.connect(('35.188.203.40',14000))
msg = x.recv(2048)
print('Message recieved: ', msg.decode())
x.close()

