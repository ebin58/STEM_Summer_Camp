import socket

def get_local_ip():
    # This creates a dummy socket connection to get your LAN IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"  # fallback to localhost
    finally:
        s.close()
    return ip

# Get local IP address
ip = get_local_ip()
port = 8888

print("Connected to Wi-Fi (assuming already connected)")
print("IP address:", ip)
print("Listening on port:", port)

# Set up UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port))

while True:
    data, addr = s.recvfrom(1024)
    message = data.decode()
    print(f"Received message: {message} from {addr}")
