# tcp_client.py
import socket

def fetch_http(host: str, port: int) -> str:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    client.send(request.encode())

    response = b""
    while True:
        data = client.recv(4096)
        if not data:
            break
        response += data

    client.close()
    return response.decode(errors="replace")

if __name__ == "__main__":
    html = fetch_http("127.0.0.1", 9998 )
    print(html)
