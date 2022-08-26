import socket
s=socket.socket()
host=socket.gethostname()
port= 1876

s.connect((host,port))
s.send(input().encode())
print(s.recv(1024).decode())

s.close()