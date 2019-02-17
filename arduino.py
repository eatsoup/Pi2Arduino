#!/usr/bin/python3

import os
import sys

if '--test' in sys.argv:
  os.system('avrdude -p atmega328p -C ~/avrdude_gpio.conf -c pi_1 -v')
elif '-s' in sys.argv:
  if len(sys.argv) < 3:
    print('Please specify file')
    sys.exit(1)
  file = sys.argv[2]
  print('Sending {} to arduino'.format(file))
  os.system('avrdude -p atmega328p -C ~/avrdude_gpio.conf -c pi_1 -v -U flash:w:{}:i'.format(file))
else:
  print('Must run as root')
  print('--test to test connection')
  print('-s file.ino.hex to send a file')

