Program your Arduino Mini Pro with a Pi
------------------------------

Use the printed numbers on the Arduino.
Count the pins on the PI (pin 2 is the closest to the corner).

GPIO Pinout
-----------
```
Arduino | PI
------------
11      | 19
12      | 21
13      | 23
RST     | 07
GND     | 09
RAW     | 02
```

Easy HOWTO
----------
 - Download and unpack https://mega.nz/#!mFdC2AyQ!qqUgYj_s14l8nkSiB_68AyQFHHK-V4VKdiUbiAq6Ybw
 - Flash the image to the PI
 - Connect and boot
 - SSH to pi (pi/raspberry)
 - sudo su
 - ./arduino.py --test

If test goes well, send your hexdump:
 - ./arduino.py -s file.ino.hex


Hard HOWTO
----------
 - Install raspbian
 - Enable SSH
 - Login as root
 - Install avrdude
 - Use avrdude config below, save as ~/avrdude_gpio.conf
 - Send file with:
 ```avrdude -p atmega328p -C ~/avrdude_gpio.conf -c pi_1 -v -U flash:w:file.cpp.hex:i```


Avrdude config
--------------
```
  id    = "pi_1";
  type  = "linuxgpio";
  reset = 4;
  sck   = 11;
  mosi  = 10;
  miso  = 9;
```
