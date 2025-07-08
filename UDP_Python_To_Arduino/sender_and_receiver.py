import socket
import threading

"""
This file is a sender file that sends messages to any device over UDP.
It also receives messages from any sender.
Made by Ebin Sebastian
"""

def receive_messages(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f"\n[Received from {addr}]: {data.decode('utf-8')}")
        except Exception as e:
            print(f"[Error receiving] {e}")

def main():
    # Local settings for binding
    local_ip = "0.0.0.0"       # Listen on all interfaces
    local_port = 8888          # You can change this if needed

    # Create and bind the socket to receive messages
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((local_ip, local_port))

    print(f"Listening on {local_ip}:{local_port} for incoming messages...\n")

    # Ask user for the destination address to send messages
    target_ip = input("Enter the IP address to send to: ").strip()
    target_port = int(input("Enter the port to send to: ").strip())

    # Send initial message
    initial_message = "Initiating connection..."
    sock.sendto(initial_message.encode(), (target_ip, target_port))
    print(f"Sent: '{initial_message}' to {target_ip}:{target_port}")

    # Start the receiver thread
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.daemon = True
    receive_thread.start()

    # Sending loop
    while True:
        message = input("\nWhat do you want to say? \n")
        if not message.strip():
            continue
        sock.sendto(message.encode(), (target_ip, target_port))

if __name__ == "__main__":
    main()
