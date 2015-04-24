#!/usr/bin/env python2

import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED2R = 9
LED2G = 11
LED2B = 0

LED1R = 13
LED1G = 6
LED1B = 5

BUTTON1 = 19
BUTTON2 = 26

STATE1 = 1
STATE2 = 1

ON = GPIO.HIGH
OFF = GPIO.LOW

def state1callback(pin):
	global STATE1
	global STATE2
	STATE1 = 0
	print "Hit Callback 1"
	print "State1 State:"
	print STATE1
	print "State2 State:"
	print STATE2

def state2callback(pin):
	global STATE1
	global STATE2
	
	if not STATE1:
		STATE2 = 0

	print "Hit Callback 2"
	print "State1 State:"
	print STATE1
	print "State2 State:"
	print STATE2

GPIO.setup(LED1R,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED1G,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED1B,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(LED2R,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2G,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(LED2B,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(BUTTON1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(BUTTON1,GPIO.FALLING,bouncetime=200)
GPIO.add_event_detect(BUTTON2,GPIO.FALLING,bouncetime=200)

GPIO.add_event_callback(BUTTON1,state1callback)
GPIO.add_event_callback(BUTTON2,state2callback)


while STATE1:
	print "State 1 must still = 1? Val ="
	print STATE1

	GPIO.output(LED1R,OFF)
	GPIO.output(LED1G,OFF)
	GPIO.output(LED1B,OFF)

	time.sleep(1)

	GPIO.output(LED1R,ON)
	GPIO.output(LED1G,OFF)
	GPIO.output(LED1B,OFF)

	time.sleep(1)

	GPIO.output(LED1R,OFF)
	GPIO.output(LED1G,ON)
	GPIO.output(LED1B,OFF)

	time.sleep(1)

	GPIO.output(LED1R,OFF)
	GPIO.output(LED1G,OFF)
	GPIO.output(LED1B,ON)

	time.sleep(1)

while STATE2:
	GPIO.output(LED2R,OFF)
	GPIO.output(LED2G,OFF)
	GPIO.output(LED2B,OFF)

	time.sleep(1)

	GPIO.output(LED2R,ON)
	GPIO.output(LED2G,OFF)
	GPIO.output(LED2B,OFF)

	time.sleep(1)

	GPIO.output(LED2R,OFF)
	GPIO.output(LED2G,ON)
	GPIO.output(LED2B,OFF)

	time.sleep(1)

	GPIO.output(LED2R,OFF)
	GPIO.output(LED2G,OFF)
	GPIO.output(LED2B,ON)

	time.sleep(1)

GPIO.cleanup()

