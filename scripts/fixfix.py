#!/usr/bin/python3

import subprocess
import time
import RPi.GPIO as GPIO


switch = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkButton():
    pass
    if (GPIO.input(switch)) == 0:
        print('pushed')
        return True
    return False

def fixStartupButton():
    print('execute fixstartup')
    subprocess.call('/home/pi/moonboard/scripts/fix_startup.sh')
    time.sleep(3)
    pass


if __name__ == '__main__':
    print('first wait some seconds')
    time.sleep(5)
    subprocess.call('/home/pi/moonboard/scripts/fix_startup.sh')
    print('fix 1')
    time.sleep(5)
    subprocess.call('/home/pi/moonboard/scripts/fix_startup.sh')
    print('fix 2')
    
    while(True):
        if checkButton():
            fixStartupButton()
        time.sleep(0.125)
    pass
