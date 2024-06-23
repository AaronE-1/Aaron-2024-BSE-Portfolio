from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

while True:
    my_input1 = int(input("Enter Servo 1 angle: "))
    kit.servo[4].angle = my_input1
    my_input2 = int(input("Enter Servo 2 angle: "))
    kit.servo[5].angle = my_input2
    my_input3 = int(input("Enter Servo 3 angle: "))
    kit.servo[6].angle = my_input3
    my_input4 = int(input("Enter Servo 4 angle: "))
    kit.servo[7].angle = my_input4