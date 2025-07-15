import socket
# This is a simple TCP client that connects to a server, sends a request, and prints the response.
# It connects to www.google.com on port 80, sends a GET request, and prints the response.

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

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
