"""
    Using pygame and serial to send signals to an arduino sketch so that the light
    on the board will turn on when X is pressed and turn off when Y is pressed
"""

import serial
import pygame
from pygame.locals import *
import time

pygame.init()
pygame.joystick.init()

# var that allows the data to goto COM6, where arduino is
arduinoData = serial.Serial('COM6', 115200)


# Check if at least one joystick is connected
if pygame.joystick.get_count() > 0:
    # Initializes the first joystick, it's really the only joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick initialized: {joystick.get_name()}")
else:
    print("No joystick found.")
    exit()


flag = False
while not flag:
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            if joystick.get_button(3):  # Y button on Xbox 360 controller
                print("Y")
                cmd = 'ON\r'
                print(cmd)
                print("")
                arduinoData.write(cmd.encode())

            if joystick.get_button(2):  # X is pressed and used to break the program
                print("X")
                cmd = 'OFF\r'
                print(cmd)
                print("")
                arduinoData.write(cmd.encode())

            if joystick.get_button(1):  # B is pressed to break
                flag = True
                cmd = 'OFF\r'
                arduinoData.write(cmd.encode())
                break


pygame.quit()
arduinoData.close()
