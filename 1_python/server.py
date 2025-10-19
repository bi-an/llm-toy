import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8080))
sock.listen(5)

while 1:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print(f"Browser sent: {data}")

    conn.send(b"HTTP/1.1 200 ok\r\nserver:yuan\r\n\r\nHello, brower")
    conn.close()
