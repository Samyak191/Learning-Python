import socket
s=socket.socket()
host=socket.gethostname()
port= 1876
s.bind((host,port))
print("waiting for connection ")
s.listen()

while True:
    conn,addr=s.accept()
    print("Got connection from", addr)
    
    print(conn.recv(1024).decode())
    conn.send((input()).encode())
    conn.close()

