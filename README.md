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

From there, download the sample scrips and run one:
```
$ git clone http://github.com/ozzmaker/BerryIMU.git
$ sudo python ./BerryIMU/python-BMP180-temperature-pressure/bmp180.py
```

If you're having problems with the board responding (e.g. IOError: [Errno 121] Remote I/O error) [wedge a watch strap under it](https://github.com/srosro/BerryWing/blob/master/sams_journal.md).
