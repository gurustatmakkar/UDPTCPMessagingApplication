import socket

x = socket.socket(type = socket.SOCK_DGRAM)

x.sendto("Gurustat Makkar".encode(), ("niagaracomputing.org", 12000) )
msg, rx_ip_port = x.recvfrom(2048)
print("MESSAGE FROM: " , rx_ip_port)
print("MESSAGE IS: " , msg.decode())
x.close()

