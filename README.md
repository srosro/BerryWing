# supradrone
A sandbox to build an autonomous drone in.

![Banner](https://github.com/srosro/supradrone/blob/master/assets/supradrone.png?raw=true)

## What I'm thinking:
I have this Raspberry Pi 2 Model B.  It has a wifi USB dongle and a 64 GB micro SD card.  I'm wondering...can I put this thing in the air? autonomously?

It's unclear whether the platform would be a quadcopter or a fixed-wing flier - to be determined.

## Things I have bought:
* [Breadboard, petentionometer switches, ultrasonic sensor, LCD screen, LEDs.](https://www.amazon.com/gp/product/B06W54L7B5) ([Howto Guide](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi))
* [Accelerometer, Gyroscope, Magnetometer and Barometric/Altitude Sensor, Temperature Sensor](https://www.amazon.com/gp/product/B072MN8ZRC) ([Sensor guides & tutorials](https://ozzmaker.com/product/berryimu-accelerometer-gyroscope-magnetometer-barometricaltitude-sensor/))
* [4G card with GPS](https://www.amazon.com/gp/product/B07PLXNVGZ) ([Manual](https://www.waveshare.com/w/upload/6/6d/SIM7600E-H-4G-HAT-Manual-EN.pdf))


## Journal
### Day 1
Breadboard kit arrived.  After much gnashing of teeth I learned that GPIO doesn't switch to hot, but instead switches to ground.  That took much longer than it should've - mostly because I don't have my voltmeter with me.  After all that I was able to flash an LED (```helloworld_LED.py```)

After that things progressed quickly.  I was able to hook up the ultrasonic sensor to the servo (```helloworld_ultraservo.py```).  As the "ground" approaches the ultrasonic sensor, the servo changes position (to adjust flight path accordingly).

[![](http://img.youtube.com/vi/hOCjklzRYUM/0.jpg)](http://www.youtube.com/watch?v=hOCjklzRYUM "First day - journal entry")


### Day 2:
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
