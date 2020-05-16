# Example python pinout program
# This will blink an LED every two seconds.

# Connect HOT (long wire) on the LED to 3.3v The GND on LED (short wire) should
# be connected to this pin (which will short to ground programmatically):
LED_GPIO = 20

import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(LED_GPIO, gpio.OUT)

try:
    while True:
        gpio.output(LED_GPIO, gpio.HIGH) #LED Off
        time.sleep(2)
        gpio.output(LED_GPIO, gpio.LOW) #LED On
        time.sleep(2)
except KeyboardInterrupt:
    gpio.cleanup()
