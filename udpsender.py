import socket

x = socket.socket(type = socket.SOCK_DGRAM)

x.sendto("PURPLE EAGLES!".encode(), ("10.128.0.2", 12000) )
#x.sendto("PURPLE EAGLES!".encode(), ("34.135.133.199", 12000) )
msg, rx_ip_port = x.recvfrom(2048)
print("MESSAGE FROM: " , rx_ip_port)
print("MESSAGE IS: " , msg.decode())
x.close()
