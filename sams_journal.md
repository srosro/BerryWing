
## Journal
### Day 1 - Hooked up Ultrasonic sensor & servo:
Breadboard kit arrived.  After much gnashing of teeth I learned that GPIO doesn't switch to hot, but instead switches to ground.  That took much longer than it should've - mostly because I don't have my voltmeter with me.  After all that I was able to flash an LED (```helloworld_LED.py```)

After that things progressed quickly.  I was able to hook up the ultrasonic sensor to the servo (```helloworld_ultraservo.py```).  As the "ground" approaches the ultrasonic sensor, the servo changes position (to adjust flight path accordingly).

[![](http://img.youtube.com/vi/hOCjklzRYUM/0.jpg)](http://www.youtube.com/watch?v=hOCjklzRYUM "First day - journal entry")


### Day 2 - 'Competitive' research:
There are some interesting Raspberry Pi drones already out there:
* [Pi Zero Plane](https://www.instructables.com/id/Pi-Zero-Plane-a-150-Smart-Fixed-Wing-Drone-With-th/) (this is the closest to what I'm looking to build).
* [DIY FPV Drone 4-axis Quadcopter Kit S500 Frame + FS-i6 Flight Control + Raspberry Pi + 920KV Motor + GPS](https://www.amazon.com/4-axis-Quadcopter-Flight-Control-Raspberry/dp/B07R7DLQGK) on Amazon.
* [Pi0drone: A $200 Smart Drone with the Pi Zero](https://www.hackster.io/12590/pi0drone-a-200-smart-drone-with-the-pi-zero-4fec08)
* [Instructables Raspberry Pi Drone](https://www.instructables.com/id/The-Drone-Pi/)
* [£300 autonomous drone with DJI Flamewheel & Ardupilot](https://medium.com/the-reading-room/how-to-build-an-autonomous-drone-for-less-than-300-80ebeb2b1db8)

There are also some interesting flying platforms:
* [2 meter wingspan, 670g payload](https://www.banggood.com/Believer-1960mm-Wingspan-EPO-Twin-Motor-Aerial-Survey-Aircraft-FPV-Platform-Mapping-RC-Airplane-KIT-p-1178800.html)
* [1.5m wingspan, "self correcting tendencies"](https://www.readymaderc.com/products/details/strix-stratosurfer-pnp)
* [2m wingspan, more advanced drone, unknown payload](https://www.readymaderc.com/products/details/rmrc-anaconda-kit)
* Long term we'll probably need something with a 3-4m wingspan [like the Penguin](https://www.uavfactory.com/product/46) (10kg payload).

We also need to start thinking about pitot tubes.  Looks like there's some prior art on an Arduino [over at MarkerPortal](https://makersportal.com/blog/2019/02/06/arduino-pitot-tube-wind-speed-theory-and-experiment).  There's also [this documentation](https://ardupilot.org/plane/docs/airspeed.html) over at [Ardupilot](https://ardupilot.org/plane/index.html).

Also... Ardupilot.  Holy smokes.  It's now the closest thing to the product we've considered.  The have a list of ready-to-fly options...

Autonomous power line inspections with image processing might be a possible use case...[see this thread with my cousin Jeremy](https://github.com/srosro/BerryWing/blob/master/assets/autonomous-power-line-monitoring-use-case.png?raw=true).


### Day 3 - Problems with BerryIMUv2:
I was having problems getting the BerryIMUv2-10DOF and get it to respond (even though the device was detected):

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

```
sudo python ./python-BMP180-temperature-pressure/bmp180.py
Traceback (most recent call last):
  File "./python-BMP180-temperature-pressure/bmp180.py", line 20, in <module>
    (chip_id, version) = bus.read_i2c_block_data(addr, 0xD0, 2)
IOError: [Errno 121] Remote I/O error
```

### Day 4 - Got the BerryIMUv2 to respond:

Found the problem: pins were not making secure contact with the board.  

Once I get my soldering gun, this will be a non-issue.  In the meantime, wedging a watch strap under the board to push it towards the pins fixed the issue:

![Wiring diagram](https://raw.githubusercontent.com/srosro/BerryWing/master/assets/watch-wedge.png)

```
$ python ./python-BMP180-temperature-pressure/bmp180.py
Chip Id: 88 Version: 0

Reading calibration data...
Starting temperature conversion...
Starting pressure conversion...
Calculating temperature...
Calculating pressure...

Temperature: 82.7 C
Pressure: -43889.54 hPa

$ python ./python-BerryIMU-gryo-accel-compass/berryIMU-simple.py

Found LSM9DS1
Loop Time  0.00 # ACCX Angle 171.88 ACCY Angle 177.32 #  	# GRYX Angle -0.03  GYRY Angle -0.01  GYRZ Angle -0.00 # 	# CFangleX Angle 103.12   CFangleY Angle 106.39 #	# HEADING 322.07  tiltCompensatedHeading 307.77 #
Loop Time  0.03 # ACCX Angle 171.92 ACCY Angle 177.41 #  	# GRYX Angle -0.31  GYRY Angle -0.14  GYRZ Angle -0.01 # 	# CFangleX Angle 144.29   CFangleY Angle 148.95 #	# HEADING 323.16  tiltCompensatedHeading 309.02 #
Loop Time  0.03 # ACCX Angle 172.07 ACCY Angle 177.28 #  	# GRYX Angle -0.61  GYRY Angle -0.25  GYRZ Angle -0.02 # 	# CFangleX Angle 160.84   CFangleY Angle 165.90 #	# HEADING 323.64  tiltCompensatedHeading 309.14 #
Loop Time  0.03 # ACCX Angle 171.95 ACCY Angle 177.43 #  	# GRYX Angle -0.90  GYRY Angle -0.37  GYRZ Angle -0.02 # 	# CFangleX Angle 167.39   CFangleY Angle 172.77 #	# HEADING 324.68  tiltCompensatedHeading 309.96 #
...
```

Now I need to work on calibration...as it's not 82.7 deg C in here...  <b>EDIT</b>: Figured it out, device is the BMP280, but the script I ran was the BMP180.  The BMP280 script works:

```
$ python ./python-BMP280-temperature-pressure/bmp280.py
Temperature in Celsius : 23.60 C
Temperature in Fahrenheit : 74.48 F
Pressure : 947.90 hPa
```

#### I also added a shutdown switch:

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


# Packages I'm installing that might be important.
I should probably put these into a python environment...

These might be useful to interface with the BerryIMU:
* ```pip3 install lsm9ds1-rjg, RPi.GPIO```

For the shutdown button:
```
apt-get install python3, python3-pip
pip3 install gpiozero
```

Also, this stuff:

```
history | grep apt-get

6  sudo apt-get install python-rpi.gpio
8  sudo apt-get install vim
29  sudo apt-get install i2c-tools libi2c-dev python-smbus
48  sudo apt-get install python-smbus
145  sudo apt-get install python-pip
171  sudo apt-get install cmake
172  sudo apt-get install python-dev
171  sudo apt-get install cmake
172  sudo apt-get install python-dev
251  apt-get search pip
255  apt-get install python3-pip
256  sudo apt-get install python3-pip
```
