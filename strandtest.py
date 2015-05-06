# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
from patchbay import create_remote_patch, Trigger, Slider
from neopixel import *

# LED strip configuration:
LED_COUNT      = 60     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Button Stuff
import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

state1 = 1
state2 = 0

BUTTON1 = 19
BUTTON2 = 26

ON = GPIO.HIGH
OFF = GPIO.LOW


#def state1callback(pin):
#	global state1
#	global state2
#	if state1:
#		state1 = not state1
#		state2 = 1

def state2callback(pin):
#	global state1
	global state2
	state2 = not state2


# Define functions which animate LEDs in various ways.
def leastAccurate(strip, color = Color(255,255,0), wait_ms=50, iteration=2):
	for j in range(iteration):
		for q in range(2):
			for i in range(0, strip.numPixels(),2):
				strip.setPixelColor(i+q,color)
			strip.show()
			#time.sleep(wait_ms/250.0)
			for i in range(0, strip.numPixels(),2):
				strip.setPixelColor(i+q,0)
def moreAccurate(strip, color = Color(255,255,0), wait_ms=50, iteration=4):
	for j in range(iteration):
		for q in range(2):
			for i in range(0, strip.numPixels(),2):
				strip.setPixelColor(i+q,color)
			strip.show()
			#time.sleep(wait_ms/500.0)
			for i in range(0, strip.numPixels(),2):
				strip.setPixelColor(i+q,0)
				
def mostAccurate(strip, color = Color(255,255,0), wait_ms=50, iteration=8):
	for j in range(iteration):
		for q in range(2):
			for i in range(0, strip.numPixels(),2):
				strip.setPixelColor(i+q,color)
			strip.show()
			#time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(),2):
				strip.setPixelColor(i+q,0)
								
def turnOnBlue(strip, color=Color(0,0,255), wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(1):
			for i in range(0, strip.numPixels(), 1):
				strip.setPixelColor(i+q, color)
			strip.show()
			#time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 1):
				strip.setPixelColor(i+q, 0)

def turnOff(strip, color=Color(0,0,0), wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
                for q in range(1):
                        for i in range(0, strip.numPixels(), 1):
                                strip.setPixelColor(i+q, color)
                        strip.show()
                        #time.sleep(wait_ms/1000.0)
                        for i in range(0, strip.numPixels(), 1):
                                strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=25):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
 

colA = [82.4,87.3,92.5,98.0,103.8,110.0,116.5,123.5,130.8,140.8,155.6,164.8,174.6,185.0,196.0,207.7,220.0,233.1,246.9,261.6,277.2,293.7,311.1,329.6,349.2,370.0,392.0,415.3,440.0,466.2,493.9,523.3,554.4,587.3]

def trigger_test(freq):
	value = freq
	range1 = 0
        range2 = 0
        range3 = 0
        range4 = 0
        range5 = 0
        range6 = 0
        range7 = 0
        range8 = 0
        range9 = 0

        i = 0
	while colA[i] <= value:
		i = i + 1

        range1 = colA[i-1]
        range9 = colA[i]
        range5 = ((range9 - range1)/2) + range1
        range3 = ((range5 - range1)/2) + range1
        range2 = ((range3 - range1)/2) + range1
        range4 = ((range5 - range3)/2) + range3
        range7 = ((range9 - range5)/2) + range5
        range6 = ((range7 - range5)/2) + range5
        range8 = ((range9 - range7)/2) + range7

        ranges = [range1,range2,range3,range4,range5,range6,range7,range8,range9]
        w = 0
        while ranges[w] <= value:
                w = w+1

        if w == 0 or  w == 7:
                turnOnBlue(strip)
        elif w == 1 or w == 6:
                mostAccurate(strip)
        elif w == 2 or w == 5:
                mostAccurate(strip)
        elif w == 3 or w == 4:
                mostAccurate(strip)

def trigger_func():
	if state2:
		theaterChaseRainbow(strip)
		return
	value = float(frequency.value) * 10

	if (value >= 587.3):
		value = 8.2
		print ("Hello")
	
	print (value)	
	range1 = 0
	range2 = 0
	range3 = 0
	range4 = 0
	range5 = 0
	range6 = 0
	range7 = 0 
	range8 = 0
	range9 = 0
	
	i = 0
	while colA[i] <= value:
		i = i + 1
	
	range1 = colA[i-1]
	range9 = colA[i]
	range5 = ((range9 - range1)/2) + range1
	range3 = ((range5 - range1)/2) + range1
	range2 = ((range3 - range1)/2) + range1
	range4 = ((range5 - range3)/2) + range3
	range7 = ((range9 - range5)/2) + range5
	range6 = ((range7 - range5)/2) + range5
	range8 = ((range9 - range7)/2) + range7

	ranges = [range1,range2,range3,range4,range5,range6,range7,range8,range9]
	w = 0
	while ranges[w] <= value:
		w = w+1
	
	if w == 0 or  w == 7:
		turnOnBlue(strip) 
	elif w == 1 or w == 6:
		mostAccurate(strip)
	elif w == 2 or w == 5:
		mostAccurate(strip)
	elif w == 3 or w == 4:
		mostAccurate(strip)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
strip.begin()

#interrupt code
GPIO.setup(BUTTON1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#GPIO.add_event_detect(BUTTON1,GPIO.FALLING,bouncetime=200)
GPIO.add_event_detect(BUTTON2,GPIO.FALLING,bouncetime=200)

#GPIO.add_event_callback(BUTTON1,state1callback)
GPIO.add_event_callback(BUTTON2,state2callback)


patch = create_remote_patch(use_udp=False)
patch.bind(channel=1, event_handler=Trigger(trigger_func))
frequency = patch.bind(channel = 2, event_handler=Slider())


while True:
	patch.route_events()	
	
	
		

				
