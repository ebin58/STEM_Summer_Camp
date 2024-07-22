from machine import Pin, PWM
import time

# Frequency doesnt matter too much

# duty_u16 sends 16 bit value, 0 to (2^16)-1
frequency = 5000

# Evan, Nelson, Mikey - Pins are 26, 27
# Mitch, Ethan, Drake - Pins are 12, 14

p1 = PWM(12, frequency)
p2 = PWM(14, frequency)

#duty_cycle = (((2**16)-1)//2)

#print(duty_cycle)

while True:
    
    per = float(input("What percent do you want the motor to spin? Enter decimal number between 0 and 1:\n"))
    
    duty_cycle = int((((2**16)-1)*per))
    
    p2.duty_u16(duty_cycle)
    p1.duty_u16(0)
    



