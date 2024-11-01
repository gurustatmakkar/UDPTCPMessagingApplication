import socket

print('Starting etcpecho.py')
x = socket.socket()
x.bind(('0.0.0.0',14000))
#x.sendall("Gurustat Makkar".encode())
#msg, rx_ip_port = x.recvfrom(2048)
x.listen(1)
while True:
        conn, addr = x.accept()
        #msg = conn.recv(2048)
        conn.sendall("Gurustat Makkar".encode())
        conn.sendall("BYE".encode())
        conn.close()
x.close()
