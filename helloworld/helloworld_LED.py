# Example python pinout program

import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)


print "Cleaning up..."
gpio.cleanup()
print "Trying again..."
gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)


while True:
    gpio.output(21, gpio.HIGH)
    print "Now high"
    time.sleep(2)
    gpio.output(21, gpio.LOW)
    print "Now low"
    time.sleep(2)
