#!/bin/bash

echo "Install services" # FIXME
cd /home/pi/moonboard/ble
make install
cd ..

cd /home/pi/moonboard/led
make install 
cd ..
