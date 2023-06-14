import RPi.GPIO as rpi
import time

message = str(input("What is your message? "))

binary = int(''.join(format(ord(i), '08b') for i in message))
print(binary)
rpi.setmode(rpi.BCM)
rpi.setup(18, rpi.OUT)
pwm = rpi.PWM(18, 433)
pwm.start(50)
for i in binary:
    if binary == 1:
        pwm.ChangeDutyCycle(75)
        time.sleep(0.25)
    if binary == 0:
        pwm.ChangeDutyCycle(25)
        time.sleep(0.25)
print("Message Sent")



