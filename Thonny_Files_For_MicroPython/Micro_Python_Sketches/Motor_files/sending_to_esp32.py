from time import sleep
from machine import Pin, PWM
import network
import socket
import time


#defining motor variables and pins
# leftMotorForward = PWM(Pin(5), freq=1000, duty_u16 = 0)
# leftMotorBackward = PWM(Pin(18), freq=1000, duty_u16 = 0)
# rightMotorForward = PWM(Pin(19), freq=1000, duty_u16 = 0)
# rightMotorBackward = PWM(Pin(21), freq=1000, duty_u16 = 0)
# rightMotorForward.duty_u16(0)
# rightMotorBackward.duty_u16(0)
# leftMotorForward.duty_u16(0)
# leftMotorBackward.duty_u16(0)

PWMFreq = 1000
DUTY_MAX = 2**16 - 1


p1 = PWM(26, PWMFreq)
p2 = PWM(27, PWMFreq)        


print("Entering code to move forward using f")
# define network related variables
netwrk = 'OAL_wireless'
password = '83792151'
port = 8888
wlan = network.WLAN(network.STA_IF)


#initializing the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 

# connects to the desired network and returns the IP address
# assigned to the esp32

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


    

# configure UDP socket, connecting to desired port

if not wlan.isconnected():
    myIp = connect()
    
sock.bind(('0.0.0.0',port))

print('waiting....')
ip = wlan.ifconfig()[0]
print(ip)

while True:
    
    data,addr = sock.recvfrom(1024)
    message = bytearray(data, 'utf-8').decode()
    print(message)
  
    if (message == 'f'):
        moveForward(DUTY_MAX, 3)
    else:
        p1.duty_u16(0)
        p2.duty_u16(0)
#         rightMotorForward.duty_u16(0)
#         rightMotorBackward.duty_u16(0)
#         leftMotorForward.duty_u16(0)
#         leftMotorBackward.duty_u16(0)