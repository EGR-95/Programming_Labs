# udp_echo_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 9997))
print("[*] Listening on 127.0.0.1:9997")

while True:
    data, addr = server.recvfrom(4096)
    print(f"[*] Received from {addr}: {data.decode()}")
    server.sendto(b"Echo: " + data, addr)

