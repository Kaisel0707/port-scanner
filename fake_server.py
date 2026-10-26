import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 2222))
s.listen()
print("listening on 2222 (Ctrl+C to stop)")
while True:
    c, _ = s.accept()
    c.send(b"SSH-2.0-FakeServer_1.0\r\n")
    c.close()
