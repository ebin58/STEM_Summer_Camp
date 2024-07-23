from time import sleep
from machine import Pin, PWM
import network
import socket
import time


netwrk = 'STEM24'
password = 'Testudo1!'
port = 8888
wlan = network.WLAN(network.STA_IF)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_to_send = "192.168.0.179"

PWMFreq = 1000
DUTY_MAX = 2**16 - 1


p1 = PWM(26, PWMFreq)
p2 = PWM(27, PWMFreq)

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

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
    
def moveForward(pwm, duration):
    
#     rightMotorForward.duty_u16(65535 // 4)
#     rightMotorBackward.duty_u16(0)
#     leftMotorForward.duty_u16(pwm)
#     leftMotorBackward.duty_u16(0)
    p1.duty_u16(pwm)
    p2.duty_u16(0)
    time.sleep(duration)
#     rightMotorForward.duty_u16(0)
#     leftMotorForward.duty_u16(0)

sock.bind(('0.0.0.0',port))

dut = 0
print("Ready to receive messages")
while True:
    
    data,addr = sock.recvfrom(1024)
    message = bytearray(data, 'utf-8').decode()
    print(message)
    if (message == 'f'):
        print("Moving forward with speed: ", dut)
        if dut != 0:
#             print("Dut if")
            moveForward(dut, 3)
        else:
#             print("Dut else")
            moveForward(DUTY_MAX, 3)
        mes = "Moving forward."
        sock.sendto(mes.encode('utf-8'), addr)
    elif is_float(message):
            message = float(message)
            print("Speed percentage is set to: ", message)
            dut = int((((2**16)-1)*message))
            print("Speed is now: ", dut)
            sock.sendto("Changing Speed".encode('utf-8'), addr)
            spee = "Speed set to: " + str(dut)
            sock.sendto(spee.encode('utf-8'), addr)
    
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