# Aaron's Three-Jointed Robotic Arm

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Aaron E | NorthStar Academy & CCU Academy | Mechanical Engineering/Robotics| Incoming Junior

<!---**Replace the BlueStamp logo below with an image of yourself and your completed project. Follow the guide [here](https://tomcam.github.io/least-github-pages/adding-images-github-pages-site.html) if you need help.**

![Headstone Image](logo.svg)
  
# Final Milestone

**Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

<iframe width="560" height="315" src="https://www.youtube.com/embed/F7M7imOVGug" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

For your final milestone, explain the outcome of your project. Key details to include are:
- What you've accomplished since your previous milestone
- What your biggest challenges and triumphs were at BSE
- A summary of key topics you learned about
- What you hope to learn in the future after everything you've learned at BSE

# Second Milestone

**Don't forget to replace the text below with the embedding for your milestone video. Go to Youtube, click Share -> Embed, and copy and paste the code to replace what's below.**

<iframe width="560" height="315" src="https://www.youtube.com/embed/y3VAmNlER5Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

For your second milestone, explain what you've worked on since your previous milestone. You can highlight:
- Technical details of what you've accomplished and how they contribute to the final goal
- What has been surprising about the project so far
- Previous challenges you faced that you overcame
- What needs to be completed before your final milestone 
-->
# First Milestone

<iframe width="951" height="535" src="https://www.youtube.com/embed/Ff5HCMyN8lo" title="Aaron E First Milestone" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

My first milestone involved assembling and testing the Cokoino robotic arm using assembly guides and sample code provided by Cokoino. Before assembling the arm, I used sample code to test the servo motors and realign their angles to 90°.

As I worked through this process, I encountered my first issue. After I tested two of the four servos, my computer stopped recognizing the Arduino Nano that is used in this project. I fixed this issue by restarting my computer, which allowed my Windows operating system to correctly identify the Nano again.

After I finished testing and aligning the servos, I continued with the assembly of the structure of the arm. Due to the small size of some of the parts, the assembly was at times difficult, but I can now control my robotic arm using the attached joysticks.

The Arduino Nano runs a program provided by Cokoino that accepts the potentiometer input of two joysticks and converts the input to the proper angles for the servos to rotate to. I will modify my project so that I can control the arm using a Raspberry Pi 4 rather than the Arduino Nano. To accomplish this, I will write a custom Python program for interfacing with the servos and joysticks.

<!---# Schematics 
Here's where you'll put images of your schematics. [Tinkercad](https://www.tinkercad.com/blog/official-guide-to-tinkercad-circuits) and [Fritzing](https://fritzing.org/learning/) are both great resoruces to create professional schematic diagrams, though BSE recommends Tinkercad becuase it can be done easily and for free in the browser. -->

# Code
[Here]([url](https://github.com/Cokoino/CKK0006/blob/master/Lesson%204%20-%20Test%20The%20Joystick%20Module/code/joystick/joystick.ino)) is the code used to test the joysticks.

[Here]([url](https://github.com/Cokoino/CKK0006/blob/master/Lesson%205%20-%20Test%20The%20Servo/code/servo_code1/servo_code1.ino)) is the code used to test the servos.

[Here]([url](https://github.com/Cokoino/CKK0006/blob/master/Lesson%206%20-%20Assembly%20The%20Robot/Code/Servo_90_ADJ/Servo_90_ADJ.ino)) is the code used to align the servos.

[Here]([url](https://github.com/Cokoino/CKK0006/tree/master/Lesson%207%20-%20Control%20The%20Robot%20Arm/Code/Arm)) is the code used to control the completed arm using the Arduino Nano. (Note: the src folder must be in the same directory as the main code for the main code to upload to the Arduino Nano correctly.)

# Bill of Materials

| **Part** | **Note** | **Price** | **Link** |
|:--:|:--:|:--:|:--:|
| Robot Arm Kit | Includes all parts for the structure of the arm, as well as the original electronics | $49.99 | <a href="[https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/](https://www.amazon.com/LK-COKOINO-Compliment-Engineering-Technology/dp/B081FG1JQ1)"> Link </a> |
| Servo Shield | Board used to connect the servos to the Arduino | $10.99 | <a href="https://www.amazon.com/HiLetgo-Expansion-Sensor-Arduino-Duemilanove/dp/B07VQRCC8F"> Link </a> |
| 9V Batteries | Provide power to system | $8.99 | <a href="https://www.amazon.com/PILOCEL-6LR61-Long-Lasting-Valentines-Leak-Proof/dp/B0BJ26CHZB?th=1"> Link </a> |
| 9V Battery Barrel Jack Connector | Connects 9V batteries to system | $5.99 | <a href="https://www.amazon.com/DZS-Elec-Connector-Experimental-5-5x2-1mm/dp/B07FDS11ZY?th=1"> Link </a> |
| Screwdriver Kit | Used for assembling parts | $7.99 | <a href="https://www.amazon.com/Small-Screwdriver-Set-Mini-Magnetic/dp/B08RYXKJW9/"> Link </a> |
| Electronics Kit | Spare electronics parts | $13.99 | <a href="https://www.amazon.com/Smraza-Electronics-Potentiometer-tie-Points-Breadboard/dp/B0B62RL725"> Link </a> |
| Digital Multimeter | Used to test various circuit parameters | $16.23 | <a href="https://www.amazon.com/AstroAI-Digital-Multimeter-Voltage-Tester/dp/B01ISAMUA6"> Link </a> |
| Raspberry Pi 4 Model B Starter Kit | Includes Raspberry Pi 4 Model B computer and necessary peripherals | $93.00 | <a href="https://www.amazon.com/Vemico-Raspberry-Starter-Heatsinks-Screwdriver/dp/B09QGZ94M8"> Link </a> |
| Servo Driver Board | Used to drive servo motors | $9.99 | <a href="https://www.amazon.com/gp/product/B0CNVBWX2M"> Link </a> |
| Analog-To-Digital Converter | Used to convert analog output signal of joysticks to digital input values for the Raspberry Pi | $9.99 | <a href="https://www.amazon.com/gp/product/B07YKH3T4C"> Link </a> |
| Portable Battery For Raspberry Pi | Used to power the Raspberry Pi without connection to wall outlet | $29.99 | <a href="https://www.amazon.com/gp/product/B0C7PHKKNK"> Link </a> |

# Other Resources/Examples
- [Original Assembly Guide & Code](https://github.com/Cokoino/CKK0006)
- [Tutorial for Using Servo Driver Board](https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview)
- [Data Sheet for External Power Supply](https://mega.nz/folder/MxgnBIDB#ygd3AMdhvgNAntwzRcWvpg/file/l1xmzZAA)
- [Pin Diagram for Raspberry Pi](https://www.youngwonks.com/blog/Raspberry-Pi-4-Pinout)
- [Tutorial for Using Analog-To-Digital Converter](https://circuitdigest.com/microcontroller-projects/interfacing-pcf8591-adc-dac-module-with-raspberry-pi)
- [Tutorial for Installing adafruit_blinka Library on Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview)
- [Fritzing Part File for External 5V Power Supply](https://github.com/RafaGS/Fritzing/blob/master/DC-DC%20Power%20Module%20(5v)%20top.fzpz)
- [Fritzing Part File for Analog-To-Digital Converter](https://github.com/adafruit/Fritzing-Library/blob/master/parts/Adafruit%20PCF8591.fzpz)
- [Circuit Diagram Tool](https://fritzing.org/)
- [Proofreading Tool](https://www.grammarly.com/)
- [Screen Recording Tool](https://www.loom.com/)
