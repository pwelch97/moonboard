# -*- coding: utf-8 -*-
import argparse
from led.moonboard import MoonBoard,LED_LAYOUT
from gi.repository import GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from functools import partial
import json 
import json
import RPi.GPIO as GPIO
import os
#import signal
import sys
import logging
import time
from BiblioPixelAnimations.matrix import *
from BiblioPixelAnimations.matrix import bloom



# external power LED and power button
LED_GPIO = 26
BUTTON_GPIO = 3


# Button function
def button_pressed_callback(channel):
    print("Button pressed") 
    MOONBOARD.clear()
    #print('Shutting down')
    #os.system("sudo shutdown -h now")


def new_problem_cb(mb,holds_string):
        holds = json.loads(holds_string)
        mb.animate_problem(holds)
        logger.debug('new_problem: '+holds_string)

if __name__ == "__main__":

    # Comment out button stuff - yet...
    # # BUTTON + LED setup
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # GPIO.setup(LED_GPIO, GPIO.OUT)
    # GPIO.output(LED_GPIO,1)
    # GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # # interupt handling for the power button
    # GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING,
    #     callback=button_pressed_callback, bouncetime=300)

    # #signal.signal(signal.SIGINT, signal_handler)
    # #signal.pause()
    time.sleep(1.5)


    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--driver_type',
                        help='driver type, depends on leds and device controlling the led.',
                        choices=['PiWS281X', 'WS2801', 'SimPixel'],
                        default='SimPixel')

    parser.add_argument('--brightness',  default=100, type=int)

    parser.add_argument('--led_layout',  
                        default=None, 
                        choices=list(LED_LAYOUT.keys())
                        )

    parser.add_argument('--debug',  action = "store_true")

    print('Start')

    args = parser.parse_args()
    argsd=vars(args)
    logger = logging.getLogger('run')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    #problems
    logger.info('start')
    led_layout = LED_LAYOUT.get(args.led_layout) if args.led_layout is not None else None
    logger.info('leds set up')
    MOONBOARD = MoonBoard(args.driver_type, led_layout)
    logger.info('moonboard set up')
    
    
    #animation=bloom.Bloom
    #MOONBOARD.run_animation(animation, run_options= {'fps': 50, 'max_cycles' : 2, 'seconds': 15})
    #MOONBOARD.stop_animation()
    #MOONBOARD.clear()
    time.sleep(1)
    MOONBOARD.clear()
    MOONBOARD.animate_tree()
    time.sleep(8)

    MOONBOARD.animate_problem({'START': [], 'MOVES': [], 'TOP': []})
    time.sleep(1)

    MOONBOARD.animate_problem({'START': ['F5'], 'MOVES': ['E8', 'H10', 'G13', 'E15'], 'TOP': ['G18']})
    
    # run led led
    #MOONBOARD.led_test()
    #MOONBOARD.clear()

    # connect to dbus signal new problem
    dbml = DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    proxy = bus.get_object('com.moonboard','/com/moonboard')

    proxy.connect_to_signal('new_problem', partial(new_problem_cb, MOONBOARD))
    loop = GLib.MainLoop()

    dbus.set_default_main_loop(dbml)

    # Run the loop
    try:
        loop.run()
    except KeyboardInterrupt:
        print("keyboard interrupt received")
    except Exception as e:
        print("Unexpected exception occurred: '{}'".format(str(e)))
    finally:
        loop.quit()
