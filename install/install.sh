#!/bin/bash

# FIXME: must run from this dir in checkout out version

#./10-prepare-raspi.sh # FIXME
#./20-prepare-python.sh # FIXME



#echo "Install application"
#test -d moonboard || git clone https://github.com/8cH9azbsFifZ/moonboard.git
#cd moonboard
#git pull

# Installing python dependencies
echo "Installing python dependencies"
pip3 install -r install/requirements.txt
sudo pip3 install -r install/requirements.txt 
# pip3 uninstall -y -r install/requirements.txt # uninstall


echo "Install services" # FIXME
cd ble
make install
cd ..
cd led
make install 
cd ..


#printf " Restarting" # FIXME
#sudo shutdown -r now
