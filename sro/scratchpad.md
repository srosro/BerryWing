## Packages I'm installing that might be important.
I should probably put these into a python environment... (EDIT: DONE!!)


To connect to the Pixhawk: https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html

`sudo apt-get install python3-dev python3-opencv python3-wxgtk3.0 libxml2-dev python3-pip python3-matplotlib python3-lxml`

Edit: python3-wxgtk3.0 doesn't seem to exist.  python3-wxgtk4.0 does...

Maybe useful:

```
history | grep apt-get

  10  sudo apt-get install modemstat
  12  sudo apt-get install minicom
  21  sudo apt-get install vim
  27  sudo apt-get install p7zip-full
  52  sudo apt-get install python3-pip
  92  sudo apt-get install screen
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


## Different hardware options

* I now realize a [6 DOF sensor](https://www.amazon.com/HiLetgo-MPU-6050-Accelerometer-Gyroscope-Converter/dp/B078SS8NQV) comes in the Freenove kit.  There's also [this 9 DOF version](https://www.amazon.com/HiLetgo-Gyroscope-Acceleration-Accelerator-Magnetometer/dp/B01I1J0Z7Y/) that's cheaper & widely supported.
* The leading Flight Controller option seems to be the [Pixhawk 2.1 Orange Cube](https://www.amazon.com/Orange-Standard-ADS-B-Carrier-Board/dp/B0842XYLGR/ref=pd_sbs_21_1/140-1966626-6294832)
* The [Navio2](https://emlid.com/navio/) is probably the most affordable, reasonable flight controller for the Raspberry Pi.  [However at $184](https://store.emlid.com/product/navio2/), it's not much cheaper than the best-in class option.
