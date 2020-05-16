# BerryWing
A sandbox to build an autonomous drone in.

![Banner](https://raw.githubusercontent.com/srosro/BerryWing/master/assets/berrywing.jpg)

## What I'm thinking:
I have this Raspberry Pi 2 Model B.  It has a wifi USB dongle and a 64 GB micro SD card.  I'm wondering...can I put this thing in the air? autonomously?

It's unclear whether the platform would be a quadcopter or a fixed-wing flier - to be determined.

## Hardware:

I already have:
* Raspberry Pi 2 Model B v1.1
* 64GB micro SD card
* WIFI USB dongle

I've bought:
* [Breadboard, petentionometer switches, ultrasonic sensor, LCD screen, LEDs.](https://www.amazon.com/gp/product/B06W54L7B5) ([Howto Guide](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi))
* [Accelerometer, Gyroscope, Magnetometer and Barometric/Altitude Sensor, Temperature Sensor](https://www.amazon.com/gp/product/B072MN8ZRC) ([Sensor guides & tutorials](https://ozzmaker.com/product/berryimu-accelerometer-gyroscope-magnetometer-barometricaltitude-sensor/)) <b>EDIT</b>: I wish I [had bought this](https://www.amazon.com/HiLetgo-Gyroscope-Acceleration-Accelerator-Magnetometer/dp/B01I1J0Z7Y/).  It seems more widely supported.
* [4G card with GPS](https://www.amazon.com/gp/product/B07PLXNVGZ) ([Manual](https://www.waveshare.com/w/upload/6/6d/SIM7600E-H-4G-HAT-Manual-EN.pdf))


## Sample code:

### Servo that responds to ultrasonic sensor:

![Wiring diagram](https://raw.githubusercontent.com/srosro/BerryWing/master/assets/ultrasonic-servo-wiring.png)

Make sure the following devices are connected to GPIO (e.g. with the breadboard and ribbon cable):

* Ultrasonic sensor:
  * Vcc: 5v (pin 02)
  * Trig: GPIO23 (pin 16)
  * Echo: GPIO24 (pin 18)
  * GND: ground
* Servo:
  * Data (yellow cable): GPIO18 (pin 12)
  * Vcc (red cable): 5v (pin 02)
  * Ground (brown cable)

Then run ```$ python helloworld_ultraservo.py```


### Getting temperature & pressure from the BerryIMUv2-10DOF:

* [Wiring guide](https://ozzmaker.com/berryimu-quick-start-guide/#BerryIMU%20wiring)
* [Enable i2c and confirm board is connected](https://ozzmaker.com/i2c/)

```
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- 1c -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- 6a -- -- -- -- --
70: -- -- -- -- -- -- -- 77
```

From there, download the sample scrips and run some:
```
$ git clone http://github.com/ozzmaker/BerryIMU.git
$ python ./BerryIMU/python-BMP280-temperature-pressure/bmp280.py

Temperature in Celsius : 23.60 C
Temperature in Fahrenheit : 74.48 F
Pressure : 947.90 hPa

$ python ./BerryIMU/python-BerryIMU-gryo-accel-compass/berryIMU-simple.py

Found LSM9DS1
Loop Time  0.00 # ACCX Angle 171.88 ACCY Angle 177.32 #  	# GRYX Angle -0.03  GYRY Angle -0.01  GYRZ Angle -0.00 # 	# CFangleX Angle 103.12   CFangleY Angle 106.39 #	# HEADING 322.07  tiltCompensatedHeading 307.77 #
Loop Time  0.03 # ACCX Angle 172.03 ACCY Angle 177.32 #  	# GRYX Angle -4.82  GYRY Angle -2.02  GYRZ Angle -0.67 # 	# CFangleX Angle 171.83   CFangleY Angle 177.24 #	# HEADING 324.22  tiltCompensatedHeading 310.00 #
Loop Time  0.03 # ACCX Angle 171.97 ACCY Angle 177.39 #  	# GRYX Angle -5.38  GYRY Angle -2.25  GYRZ Angle -0.69 # 	# CFangleX Angle 171.78   CFangleY Angle 177.31 #	# HEADING 324.67  tiltCompensatedHeading 309.89 #
...
```

If you're having problems with the board responding (e.g. IOError: [Errno 121] Remote I/O error) [wedge a watch strap under it](https://github.com/srosro/BerryWing/blob/master/sams_journal.md).


### Graceful shutdown with a push-button switch:
There's no power switch on the raspberry pi (a pet peeve of mine).  Kids are always unplugging things, and I hate it when my Pi is unplugged while running!

It's easy to set up a "shutdown" switch (though you'll still have to power-cycle to start the pi):

Wire the [small black momentary push button switch](https://www.sparkfun.com/products/9190) between GPIO21 & GND on the Raspberry Pi.  Then:  

```
apt-get install python3, python3-pip
pip3 install gpiozero
chmod a+x ~/berrywing/helloworld/shutdown-press.py
sudo nano /etc/rc.local
```

and add this line before ```exit 0``` at the end of rc.local:

```
sudo -H -u pi /usr/bin/python3 /home/pi/berrywing/helloworld/shutdown-press.py &
```

[More details here](https://github.com/TonyLHansen/raspberry-pi-safe-off-switch).s
