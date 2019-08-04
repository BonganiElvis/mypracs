#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Bongani Gqweta>
Student Number: <GQWBN002>
Prac: <Prac_1>
Date: <04/08/2019>
"""

# importing Relevant Librares
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=16
button2=32
LED1=22
LED2=18 
LED3=36
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)

GPIO.output(LED1,GPIO.LOW)
GPIO.output(LED2,GPIO.LOW)
GPIO.output(LED3,GPIO.LOW)
counter = 0
#Push Button Logic 
def buttonHandler():
	global counter
	if (GPIO.input(button2) == 1 and counter != 7): # incrementing the counter by 1
		counter += 1
		print (bin(counter)[2:].zfill(3))
		sleep(.5)
	if (GPIO.input(button2) == 1 and counter == 7):
		counter = 0
		print (bin(counter)[2:].zfill(3))
		sleep(.5)
	if (GPIO.input(button1) == 1 and counter != 0): #stop decrementing of inputs if 0
		counter -= 1
		print (bin(counter)[2:].zfill(3))
		sleep(.5)
	if (GPIO.input(button1) == 1 and counter == 0):
		counter = 7
		print (bin(counter)[2:].zfill(3))
		sleep(.5)
	return
