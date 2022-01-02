#!/bin/bash

echo "Install services" # FIXME
cd ble
make install
cd ..

cd led
make install 
cd ..
