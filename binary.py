#!/bin/usr/env python

sec = [ "11", "01", "10", "00" ]
sec1 = "11"
sec2 = "01"
sec3 = "10"
sec4 = "00"

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
for x in range(0, 4):
	print("")
	cur = list(sec[x])
	if cur[0] == '1':
		print("Setting 17 to HIGH")
		GPIO.output(17,GPIO.HIGH)
	else:
		print("Setting 17 to LOW")
		GPIO.output(17,GPIO.LOW)
	
	if cur[1] == '1':
		print("Setting 16 to HIGH")
		GPIO.output(16,GPIO.HIGH)
	else:
		print("Setting 16 to LOW")
		GPIO.output(16,GPIO.LOW)
	
	print("")
	time.sleep(1)

# GPIO.output(17,GPIO.HIGH)
