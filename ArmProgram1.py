#import needed libraries

import smbus

import time

from adafruit_servokit import ServoKit

#set up top-level variables

address = 0x48

A0 = 0x40

bus = smbus.SMBus(1)

kit = ServoKit(channels=16)

currentAngle = 90

#main loop
    
while True:

    bus.write_byte(address,A0)

    value = bus.read_byte(address)
    
    if value >= 211:
        
        desiredAngle = (45/22) * (value - 211) + 90
    
    else:
        
        desiredAngle = (90/211) * (value)
    
    while abs((currentAngle - desiredAngle)) > 3:
        
        if currentAngle > desiredAngle:
            
            currentAngle = currentAngle - 3
        
        if currentAngle < desiredAngle:
            
            currentAngle = currentAngle + 3

        kit.servo[4].angle = currentAngle
        
        time.sleep(0.1)
    
    print(value,currentAngle)