import socket

"""
This file is a basic sender file that send 
"""


localIP = "192.168.0.224"
udpPort = 8888
message = "Initiating connection..."

print("UDP target IP: %s" % localIP)
print("UDP target port: %s" % udpPort)
print("message: %s" % message)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(message,"utf-8"), (localIP, udpPort))

while True:
    message = input("What do you want to say? \n")

    sock.sendto(bytes(message, "utf-8"), (localIP, udpPort))
