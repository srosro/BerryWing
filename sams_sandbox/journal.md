
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

### Day 5 - More research:

Okay, going to take some time to write out what I know so far:

#### Startups in autonomous flight:
* [Zipline](https://flyzipline.com/) is the leading startup in this space, and [now valued at 1BN+](https://www.cnbc.com/2019/05/17/zipline-medical-delivery-drone-start-up-now-valued-at-1point2-billion.html)
* [Matternet](https://mttr.net/) is focused on automated drone delivery, but seems further behind Zipline.


#### Useful proof-of-concept tech:
* [Ardupilot](https://ardupilot.org/) is the leading open source community for autonomous drones.
* [Pixhawk](https://pixhawk.org/) = an open source flight controller. Seems like a very useful interface between the Raspberry Pi and the control surfaces of the plane.
* Ardupilot worked with Pixhawk to build the [Pixhawk 2.1 Cube](https://www.amazon.com/Standard-Carrier-Board-Pixhawk-2-1/dp/B071L846SN/), which was a massive improvement on the original [Pixhawk](https://www.amazon.com/Readytosky-Pixhawk-Controller-Autopilot-Splitter/dp/B07CHQ7SZ4?ref_=fsclp_pl_dp_1)
* Ardupilot had a falling out with Pixhawk.  Pixhawk went on to build the Pixhawk 4, which seems to be [regarded as inferior to the Pixhawk 2.1 Cube](https://www.youtube.com/watch?v=C6WxNIzl8HU).
* The leading option seems to be the [Pixhawk 2.1 Orange Cube](https://www.amazon.com/Orange-Standard-ADS-B-Carrier-Board/dp/B0842XYLGR/ref=pd_sbs_21_1/140-1966626-6294832)
* [Connecting Raspberry Pi w/ Pixhawk and Communicating via MAVLink Protocol](https://www.youtube.com/watch?v=DGAB34fJQFc) or [this video](https://www.youtube.com/watch?v=cZVNndOaYCE) both cover connecting to the original Pixhawk.
* [MAVLink](https://mavlink.nebraska.edu/psp/mavlink/NBO/HRMS/?cmd=login): A drone <-> ground control communication protocol.
* [Dronekit](https://dronekit.io): a python interface for MAVLink.


#### Electric human flight:
Airbus, Rolls Royce, Wright Electric are all building prototypes - but nothing is close to production.

In my opinion, this is the wrong place to start - as the startup is too far from profitability.  The winning play is to focus on autonomous fleets of small planes (like Zipline) as graduating to larger vehicles (and then vehicles that carry humans) is two incremental steps from there.

* Also not yet in production, but supposedly [Otto Aviation](http://ottoaviation.com/) is building [an electric plane as efficient as a car](https://www.thedailybeast.com/this-weird-plane-could-be-the-prius-of-the-skies).
*  [ALPHA Electro](https://www.pipistrel-usa.com/alpha-electro/) is the first [FAA certified electric trainer](https://electrek.co/2018/04/27/all-electric-trainer-plane-airworthiness-certification-faa-us/).  It's an interesting first use case for electric, since sorties are short and trainers compete on efficiency.
* Not electric, but [Jetpack Aviation sells a human jetpack](https://jetpackaviation.com/jetpacks/).
* The [Ehang 184](https://www.ehang.com/ehangaav) seems to be the closest to a passenger autonomous drone.

#### 3D imaging:

The standard of art is LIDAR + imaging, which is already being used in the power line inspection space.

* [Matterport](https://matterport.com/) seems to be the leading startup, but their most used interface isn't really a usable 3D model.  It's closer to Google maps ([see demo](https://matterport.com/industries/gallery/piedmont-heights-clubroom)).
* The city of Christchurch worked with [AAM Group](http://www.aamgroup.com/index-nz.htm) to [use LIDAR and imaging](https://smartchristchurch.org.nz/project/christchurch-cbd-models-and-visualisations/) to create a [3D model of the city](http://cccbeforeafter.digitalnewzealand.info).
* The [iPad 3D Camera/LIDAR system](https://www.theverge.com/2020/4/16/21223626/ipad-pro-halide-camera-lidar-sensor-augmented-reality-scanning) will be coming out on the iPhone 12 and seems like it will dramatically change this space.

#### Power line imaging:
* The common solution is LIDAR + photography ([like this](https://greenvalleyintl.com/applications/power-line-inspection-using-airborne-lidar/))
* [Flytech](https://www.flytechuav.com) [doesn't use LIDAR](https://www.suasnews.com/2019/08/how-photogrammetry-will-replace-lidar-in-transmission-line-inspections/).  They've built hardware & software close to what I'm thinking about - but it's not autonomous.  Their business model is to [sell the hardware](https://www.flytechuav.com/uav-birdie.html) which would be different than what I was thinking.
* PG&E pays [~1.25bn / year to inspect power lines](https://www.courthousenews.com/utility-watchdog-oks-pge-wildfire-preventioin-plan/).

Regarding geographic location: Seems like you'd want to consider geographies that have high fire risk and also are densely populated near forests with high property values.  Based [on this map](https://data.giss.nasa.gov/impacts/gfwed/), maybe options like this:
* Western US (California, Montana, Utah Wyoming, Nevada)
* Israel
* Australia
* Spain
* Southern Italy

California really does seem like the ideal location to do this, though.  There probably isn't a huge market beyond the annual spend of PG&E...

### Day 6 - The research continues...

* I have successfully loaded Ardupilot firmware on the Pixhawk 2.1 Orange Cube, using QGroundControl.  I've been able to configure compass & accelerometer/gyroscope.
* I'm having some trouble with APM Planner 2.0 on a mac, [documented here](https://discuss.ardupilot.org/t/ftdi-drivers-incompatible-with-max-os-x-10-15-4/56853).  Might need a netbook or something...
* I need to [watch this video](https://www.youtube.com/watch?v=cZVNndOaYCE) about connecting the Raspberry Pi to the Pixhawk 2.1 Cube.  Also this [video looks interesting](https://www.youtube.com/watch?v=3ktSk3jGm4I) (a simulation).
* This guide explains exactly what I'm looking to do: [Unlimited range HD streaming with LTE](https://discuss.ardupilot.org/t/unlimited-range-hd-streaming-with-lte/48670).  The Raspberry Pi can then handle increasing amounts of autopilot logic (for example, using signals from the video camera input to set the direction of the plan, tracking a power line).


The [FLYSKY FS-i6X 10CH 2.4GHz RC Transmitter Controller](https://www.amazon.com/gp/product/B07Z8VCB45/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1) that I purchased, I believe is compatible with the Pixhawk 2.1 Cube using either the PPM-Sum or IBUS protocols..See these links:
* [FlySky Fs-IA6B Receiver](https://www.rcgroups.com/forums/showthread.php?2968555-FlySky-Fs-IA6B-Receiver)
* [Compatible RC Transmitter and Receiver Systems](https://ardupilot.org/copter/docs/common-pixhawk-and-px4-compatible-rc-transmitter-and-receiver-systems.html)
* [Using PPM for FlySky I6X Transmitter with I6B Reciever and NAZE32](https://www.youtube.com/watch?v=wBG4BgtGxLQ)
* [Flysky FS-i6 6CH 2.4G AFHDS with Pixhawk and PX4?](https://diydrones.com/forum/topics/flysky-fs-i6-6ch-2-4g-afhds-with-pixhawk-and-px4)
* [Good receiver with FlySky FS-i6 and Pixhawk or HK32Pilot Flight controller.](https://www.amazon.com/review/RFV9HKOWYYTS4/ref=cm_cr_srp_d_rdp_perm)
