from time import sleep
from machine import Pin, PWM
import network
import socket
import time

"""
This file was made by Natalie but edited by Ebin.
It is used to receive messages and if it receives the letter f, it will move the
defined motor forward
"""

netwrk = 'STEM24'
password = 'Testudo1!'
port = 8888
wlan = network.WLAN(network.STA_IF)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


PWMFreq = 1000
DUTY_MAX = 2**16 - 1


p1 = PWM(12, PWMFreq)
p2 = PWM(14, PWMFreq)

p1.duty_u16(0)
p2.duty_u16(0)



def connect():
    wlan.active(True)
    while not wlan.isconnected():
    
      print("Waiting to connect...")
      wlan.connect(netwrk, password)
      time.sleep(2)
      
    ip = wlan.ifconfig()[0]
    print("Successfully connected to ", netwrk)
    print("ip address: ", ip)
    return ip

if not wlan.isconnected():
    myIp = connect()


def moveForward(pwm, duration):
    
#     rightMotorForward.duty_u16(65535 // 4)
#     rightMotorBackward.duty_u16(0)
#     leftMotorForward.duty_u16(pwm)
#     leftMotorBackward.duty_u16(0)
    p1.duty_u16(65535//4)
    p2.duty_u16(0)
    time.sleep(duration)
#     rightMotorForward.duty_u16(0)
#     leftMotorForward.duty_u16(0)

sock.bind(('0.0.0.0',port))


while True:
    
    data,addr = sock.recvfrom(1024)
    message = bytearray(data, 'utf-8').decode()
    print(message)
  
    if (message == 'f'):
        print("Moving forward")
        moveForward(DUTY_MAX, 3)
    else:
        print("Stopping")
        p1.duty_u16(0)
        p2.duty_u16(0)
#         rightMotorForward.duty_u16(0)
#         rightMotorBackward.duty_u16(0)
#         leftMotorForward.duty_u16(0)
#         leftMotorBackward.duty_u16(0)
# print('waiting....')
# ip = wlan.ifconfig()[0]
# print(ip)