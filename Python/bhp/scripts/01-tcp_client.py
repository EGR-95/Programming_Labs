import socket

host = "www.google.com"
port =80 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

request = b"GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n"
client.send(request)

response = b""
while True:
    data = client.recv(4096)
    if not data:
        break
    response += data

print(response.decode(errors="replace"))
client.close()

