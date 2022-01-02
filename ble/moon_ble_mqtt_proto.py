import sys
from gatt_base.gatt_lib_advertisement import Advertisement
from gatt_base.gatt_lib_characteristic import Characteristic
from gatt_base.gatt_lib_service import Service
import string,json
import subprocess
import logging
from moonboard_app_protocol import UnstuffSequence, decode_problem_string

import os
import threading
import pty
 
BLUEZ_SERVICE_NAME =           'org.bluez'
LE_ADVERTISING_MANAGER_IFACE = 'org.bluez.LEAdvertisingManager1'
GATT_MANAGER_IFACE =           'org.bluez.GattManager1'
GATT_CHRC_IFACE =              'org.bluez.GattCharacteristic1'
UART_SERVICE_UUID =            '6e400001-b5a3-f393-e0a9-e50e24dcca9e'
UART_RX_CHARACTERISTIC_UUID =  '6e400002-b5a3-f393-e0a9-e50e24dcca9e'
UART_TX_CHARACTERISTIC_UUID =  '6e400003-b5a3-f393-e0a9-e50e24dcca9e'
LOCAL_NAME =                   'Moonboard A'

class RxCharacteristic(Characteristic):
    def __init__(self, bus, index, service, process_rx):
        Characteristic.__init__(self, bus, index, UART_RX_CHARACTERISTIC_UUID,
                                ['write'], service)
        self.process_rx=process_rx

    def WriteValue(self, value, options):
        pass
        #self.process_rx(value)

class UartService(Service):
    def __init__(self, bus,path, index, process_rx):
        Service.__init__(self, bus,path, index, UART_SERVICE_UUID, True)
        self.add_characteristic(RxCharacteristic(bus, 1, self, process_rx))       

class OutStream:
    def __init__(self, fileno):
        self._fileno = fileno
        self._buffer = b""

    def read_lines(self):
        try:
            output = os.read(self._fileno, 1000)
        except OSError as e:
            if e.errno != errno.EIO: raise
            output = b""
        lines = output.split(b"\n")
        lines[0] = self._buffer + lines[0] # prepend previous
                                           # non-finished line.
        if output:
            self._buffer = lines[-1]
            finished_lines = lines[:-1]
            readable = True
        else:
            self._buffer = b""
            if len(lines) == 1 and not lines[0]:
                # We did not have buffer left, so no output at all.
                lines = []
            finished_lines = lines
            readable = False

        finished_lines = [line.rstrip(b"\r")
                         for line in finished_lines]
        
        return finished_lines, readable


class MoonApplication():
    def __init__(self):
        return


    def monitor_btmon(self): 
        out_r, out_w = pty.openpty()
        cmd = ["sudo","btmon"]
        process = subprocess.Popen(cmd, stdout=out_w)
        f = OutStream(out_r)
        while True:
            lines, readable = f.read_lines()
            if not readable: break
            for line in lines:                
                if line != '':
                    line = line.decode()
                    if 'Data:' in line:
                        data = line.replace(' ','').replace('\x1b','').replace('[0m','').replace('Data:','')
                        self.process_rx(data)
                        #self.logger.info('New data '+ data)

    def process_rx(self,ba):
        new_problem_string= self.unstuffer.process_bytes(ba)
        flags = self.unstuffer.flags

        if new_problem_string is not None:
            problem= decode_problem_string(new_problem_string, flags)
            self.new_problem(json.dumps(problem))
            self.unstuffer.flags = ''
            start_adv()

def setup_adv(logger):
    """
    Setup Advertisinf"""
    logger.info('setup adv')
    setup_adv = [
    "hcitool -i hci0 cmd 0x08 0x000a 00",
    "hcitool -i hci0 cmd 0x08 0x0008 18 02 01 06 02 0a 00 11 07 9e ca dc 24 0e e5 a9 e0 93 f3 a3 b5 01 00 40 6e 00 00 00 00 00 00 00",
    "hcitool -i hci0 cmd 0x08 0x0009 0d 0c 09 4d 6f 6f 6e 62 6f 61 72 64 20 41",
    "hcitool -i hci0 cmd 0x08 0x0006 80 02 c0 03 00 00 00 00 00 00 00 00 00 07 00"
    ]
    for c in setup_adv:
        os.system("sudo "+ c) 


def start_adv(logger,start=True):
    """
    Start Advertising 
    """
    if start:
        start='01'
        logger.info('start adv')
    else:
        start='00'
        logger.info('stop adv')
    start_adv= "hcitool -i hci0 cmd 0x08 0x000a {}".format(start)
    os.system("sudo " +start_adv) 

def main(logger,adapter):
    logger.info("Bluetooth adapter: "+ str(adapter))
    app = MoonApplication()    
    
    setup_adv(logger)
    start_adv(logger)

 
if __name__ == '__main__':
    
    import argparse
    parser = argparse.ArgumentParser(description='Moonboard bluetooth service')
    parser.add_argument('--debug',  action = "store_true")

    args = parser.parse_args()
    argsd=vars(args)

    logger = logging.getLogger('moonboard.ble')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    main(logger,adapter='/org/bluez/hci0')
