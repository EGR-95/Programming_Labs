# tcp_client.py
import socket
from typing import Optional

def fetch_http(host: str, port: int = 80, timeout: float = 5.0) -> Optional[str]:
    try:
        # Create a TCP connection with timeout
        with socket.create_connection((host, port), timeout=timeout) as client:
            request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
            client.sendall(request.encode())

            response = b""
            while True:
                data = client.recv(4096)
                if not data:
                    break
                response += data

        return response.decode(errors="replace")
    
    except socket.gaierror:
        print(f"[!] DNS resolution failed for {host}")
    except ConnectionRefusedError:
        print(f"[!] Connection refused by {host}:{port}")
    except socket.timeout:
        print(f"[!] Connection to {host}:{port} timed out")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
    
    return None

if __name__ == "__main__":
    # 👤 User input
    host = input("Enter target IP or hostname (e.g. 127.0.0.1 or www.google.com): ").strip()
    
    # Validate port input
    try:
        port = int(input("Enter port number (e.g. 80 or 9998): ").strip())
    except ValueError:
        print("[!] Invalid port. Please enter a number.")
        exit(1)

    print(f"[*] Connecting to {host}:{port} ...")
    html = fetch_http(host, port)

    if html:
        print("[+] Response received:\n")
        print(html)
    else:
        print("[-] No response received.")
