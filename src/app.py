import socket

s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen(1)

c, _ = s.accept()
s.close()
c.sendall(b"Hello World\n")
c.close()
