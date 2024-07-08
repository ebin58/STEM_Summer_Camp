"""
    Sends a message to an ip address and port specific by the user
    So far it is used to primarily to send commands to arduino

"""

import keyboard
import socket


# Asks user for the last three digits of their ip address. If it is at the USMSM lab room, then it should
# start with 192.168.0
three_digit = input("What is your ip address? Enter last three digits:\n")


# This is my laptops IP address
my_ip_address = "192.168.0."+three_digit

# port we are going to be connecting to, nothing should be connected to it
localUDPPort = int(input("Please enter port you want to connect to:\n"))

# creating a socket so that it makes a connection to the port
# SOCKET.AF_INET -> Specific IP address you are looking for <- IPV4
# socket.SOCK_DGRAM -> Saying what wr are sending <- DGRAM = datagram
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


flag = False
command_flag = False

while not flag:

    courtesy = input("Press K for UDLR, press M for typing messages, E to escape: \n")

    if courtesy.upper() == 'E':
        flag = True

    if courtesy.upper() == "K":
        command_flag = False
        while not command_flag:
            print("Enter keyboard command, press esc to exit: \n")
            send_flag = False
            event = keyboard.read_event()
            message = "No key entered"

            if event.event_type == 'down' and event.name == 'up':
                print("up is pressed")
                message = "pressed up key"
                send_flag = True

            if event.event_type == 'down' and event.name == 'down':
                print("down is pressed")
                message = "pressed down key"
                send_flag = True

            if event.event_type == 'down' and event.name == 'left':
                print("left is pressed")
                message = "pressed left key"
                send_flag = True

            if event.event_type == 'down' and event.name == 'right':
                print("right is pressed")
                message = "pressed right key"
                send_flag = True

            if event.event_type == 'down' and event.name == 'esc':
                print("\nesc is pressed, leaving.\nGoodbye!!")
                message = "pressed esc key"
                send_flag = True
                command_flag = True

            if send_flag:
                sock.sendto(bytes(message, "utf-8"), (my_ip_address, localUDPPort))

    if courtesy.upper() == "M":
        word_flag = False
        while not word_flag:
            message = input("What is the message you want to send?\nType on to turn LED on\nType off to turn LED "
                            "off\nPress 'e' to exit:\n")

            # sending the message
            sock.sendto(bytes(message, "utf-8"), (my_ip_address, localUDPPort))

            if message == "e":
                word_flag = True