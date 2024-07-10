import pygame
from pygame.locals import *
import time

pygame.init()
pygame.joystick.init()

# Check if at least one joystick is connected
if pygame.joystick.get_count() > 0:
    # Initializes the first joystick, its really the only joystick
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
            if joystick.get_button(3):  # Button 3 corresponds to the Y button on Xbox 360 controller
                print("Y")

            if joystick.get_button(2):
               flag = True
               break

        elif event.type == JOYAXISMOTION:
          print(f"Axis {event.axis} moved to {event.value}")
          # time.sleep(1)

        elif event.type == JOYHATMOTION:
          print("Hatstick has been pressed")


pygame.quit()
