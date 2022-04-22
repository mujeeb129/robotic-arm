import RPi.GPIO as GPIO
from time import sleep


class MotorControl():
    
    def __init__(self):
        #declaring variables
        leftMotor1 =
        leftMotor2 =
        enLeftMotor =

        rightMotor1 =
        rightMotor2 =
        enRightMotor =

        #setup
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(leftMotor1 , GPIO.OUT)
        GPIO.setup(leftMotor2 , GPIO.OUT)
        GPIO.setup(enLeftMotor , GPIO.OUT)

        GPIO.setup(rightMotor1 , GPIO.OUT)
        GPIO.setup(rightMotor2 , GPIO.OUT)
        GPIO.setup(enRightMotor , GPIO.OUT)

        leftSpeed = GPIO.PWM(enLeftMotor, 1000)
        rightSpeed = GPIO.PWM(enRightMotor, 1000)
        print('#STARTING_MOTOR \n#LEFT_SPEED=25%\t#RIGHT_SPEED=25%')
        leftSpeed.start(25)
        rightSpeed.start(25)

        
