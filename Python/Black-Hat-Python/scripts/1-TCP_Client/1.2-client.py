import socket

target_host = "127.0.0.1"
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send(b"Hello, Server!")
response = client.recv(4096)
print(response.decode())
client.close()

