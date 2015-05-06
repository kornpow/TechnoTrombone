import time
import sys
import RPi.GPIO as GPIO


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
