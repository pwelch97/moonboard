#!/bin/bash

# FIXME: must run from this dir in checkout out version

#./10-prepare-raspi.sh # FIXME
#./20-prepare-python.sh # FIXME

echo "Install DBUS service" # FIXME
sudo cp /home/pi/moonboard/ble/com.moonboard.conf /etc/dbus-1/system.d
sudo cp /home/pi/moonboard/ble/com.moonboard.service /lib/systemd/system/com.moonboard.service
sudo chmod 644 /lib/systemd/system/com.moonboard.service
sudo systemctl daemon-reload
sudo systemctl enable com.moonboard.service
sudo systemctl restart com.moonboard.service


echo "Install service for Moonboard app" 
sudo cp /home/pi/moonboard/services/moonboard.service /lib/systemd/system/moonboard.service
sudo chmod 644 /lib/systemd/system/moonboard.service 
sudo systemctl daemon-reload
sudo systemctl enable moonboard.service
sudo systemctl restart moonboard.service


#printf " Restarting" # FIXME
#sudo shutdown -r now
