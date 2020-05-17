#!/usr/bin/env python3
from gpiozero import Button
import os

# This file will initiate the Raspberry Pi shutdown sequence
# when the user presess a physical button.

# The GPIO pin that the shutdown button installed shorts to ground:
SHUTDOWN_GPIO = 21

Button(SHUTDOWN_GPIO).wait_for_press()
os.system("sudo poweroff")
