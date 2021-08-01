FROM debian:latest

RUN apt-get -y update && apt-get upgrade
RUN apt-get -y install git vim python3-pip gcc make build-essential libatlas-base-dev python-dev swig scons 

WORKDIR /ble 
ADD . /ble/

#https://georgik.rocks/how-to-start-d-bus-in-docker-container/
#dbus-uuidgen > /var/lib/dbus/machine-id
#mkdir -p /var/run/dbus
#dbus-daemon --config-file=/usr/share/dbus-1/system.conf --print-address
#python3 moonboard_BLE_service.py 