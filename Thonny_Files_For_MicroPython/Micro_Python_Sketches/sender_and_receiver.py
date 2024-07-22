import socket
import threading

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print("Receiving messages")
        print("\nReceived message: %s" % data.decode('utf-8'))

def main():
    localIP = "192.168.0.224"
    udpPort = 8888
    message = "Initiating connection..."

    print("UDP target IP: %s" % localIP)
    print("UDP target port: %s" % udpPort)
    print("message: %s" % message)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(message, "utf-8"), (localIP, udpPort))

    # Start the thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        message = input("What do you want to say? \n")
        sock.sendto(bytes(message, "utf-8"), (localIP, udpPort))

if __name__ == "__main__":
    main()
