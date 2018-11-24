Program your Arduino Mini Pro with a Pi
------------------------------

Use the printed numbers on the arduino.
Count the pins on the pi (pin 2 is the closest to the corner).

GPIO Pinout:
 - Arduino | Pi
 - 11      | 19
 - 12      | 21
 - 13      | 23
 - RST     | 07
 - GND     | 09
 - RAW     | 02

Avrdude config:
----------------
  type  = "linuxgpio";
  reset = 4;
  sck   = 11;
  mosi  = 10;
  miso  = 9;


Easy HOWTO
-----
 - Flash the image to the PI
 - Connect and boot
 - SSH to pi (pi/raspberry)
 - sudo su
 - ./arduino.py --test

If test goes well, send your hexdump:
 - ./arduino.py -s file.ino.hex
