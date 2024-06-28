import time
import smbus
from adafruit_servokit import ServoKit

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)
kit = ServoKit(channels=16)

delta_x = 0.1  # change in angle here
threshold = 10  # change required forupdate
center = 90  # center point
lim_pos = 170  # positive limit
lim_neg = 10  # negative limit

bus.write_byte(address, A0)
def_val1 = bus.read_byte(address)

bus.write_byte(address, A0+1)
def_val2 = bus.read_byte(address)

bus.write_byte(address, A0+2)
def_val3 = bus.read_byte(address)

bus.write_byte(address, A0+3)
def_val4 = bus.read_byte(address)


def translation(input_pin, output_pin, angle, last_time, def_val):

    if (time.time() - last_time) > 0.1:  # change based on update time
        # get joystick angle
        bus.write_byte(address, A0+input_pin)
        val = bus.read_byte(address)
        
        print(val)

        if val >= def_val:
            new_angle = (90/(255-def_val)) * (val - def_val) + 90
        else:
            new_angle = (90/def_val) * (val)

        # detect if angle is outside the threshold (prevent noise)
        if abs(new_angle - center) > threshold:
            angle = angle + delta_x * (new_angle-center)  # update angle
            if angle > lim_pos:  # check for saturation
                angle = lim_pos
            if angle < lim_neg:  # check for saturation
                angle = lim_neg
            kit.servo[4+output_pin].angle = angle  # write the angle
        
        last_time = time.time()  # update the last update time

    return angle, last_time


angle_1 = angle_2 = angle_3 = angle_4 = 90
last_t_1 = last_t_2 = last_t_3 = last_t_4 = time.time()

kit.servo[4].angle = 90
kit.servo[5].angle = 90
kit.servo[6].angle = 90
kit.servo[7].angle = 90

while True:
    #X1 (Right, V), Servo 1 (Lower Arm)
    angle_1, last_t_1 = translation(0, 0, angle_1, last_t_1, def_val1)
        
    #Y1 (Right, H), Servo 2 (Upper Arm)
    angle_2, last_t_2 = translation(1, 1, angle_2, last_t_2, def_val2)
        
    #X2 (Left, V), Servo 3 (Gripper)
    angle_3, last_t_3 = translation(2, 2, angle_3, last_t_3, def_val3)
        
    #Y2 (Left, H), Servo 1 (Base)
    angle_4, last_t_4 = translation(3, 3, angle_4, last_t_4, def_val4)