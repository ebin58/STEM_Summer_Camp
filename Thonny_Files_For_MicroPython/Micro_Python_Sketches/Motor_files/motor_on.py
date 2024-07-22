from machine import Pin, PWM
import time

# Replace num with the num with the pin numbers

#Both teams are good for motor, they are turned on

# Evan, Nelson, Mikey - Pins are 26, 27
# Mitch, Ethan, Drake - Pins are 12, 14


p1 = Pin(12, Pin.OUT)
p2 = Pin(14, Pin.OUT)


p1.value(1)
p2.value(0)