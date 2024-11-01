# This application will listen for UDP packets.
# It will print the sender address (port and IP)
# and the packet contents (message /payload)
import socket

print("running udplisterner.py")
#create a socket object
#x = socket.socket() # This is for TCP
x = socket.socket(type = socket.SOCK_DGRAM)
x.bind(("0.0.0.0",12000))

#print(("apple", "pear", "berries"))

# bind the socket to ANY IP and port 12000
msg, rx_ip_port = x.recvfrom(2048)
print("MESSAGE FROM: " , rx_ip_port)
print("MESSAGE IS: " , msg.decode())
x.sendto('PURPLE EAGLES!'.encode(),rx_ip_port)
print('Message sent')
x.close()

