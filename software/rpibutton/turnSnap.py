#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

def set(property, value):
    try:
        f = open('/sys/class/rpi-pwm/pwm0/' + property, 'w')
        f.write(value)
        f.close()	
    except:
        print('Error writing to: ' + property + " value: " + value)

def setServo(angle):
	set('servo', str(angle))
	
		
set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")

delay_period = 3 

def rotateSnap():
	for angle in range(0, 180,45):
		setServo(angle)
		os.system('fswebcam test.jpeg')
		sleep(delay_period)
	for angle in range(0, 180,45):
		setServo(180 - angle)
		os.system('fswebcam test.jpeg')
		sleep(delay_period)

while True:
        if ( GPIO.input(25)== False ):
		print "switch connected"
		setServo(45)
		sleep(1)
		os.system('fswebcam test.jpeg')
		sleep(2)
		setServo(90)
		sleep(1)
		os.system('fswebcam test.jpeg')
                sleep(2)
	else:
		print "waiting ..."        
	sleep(0.1);

