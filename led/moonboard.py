# -*- coding: utf-8 -*-
from bibliopixel.colors import COLORS
from bibliopixel import Matrix
from bibliopixel.drivers.PiWS281X import PiWS281X
from bibliopixel.drivers.dummy_driver import DriverDummy
from bibliopixel.drivers.SPI.WS2801 import  WS2801
from bibliopixel.drivers.PiWS281X import  PiWS281X
from bibliopixel.drivers.SimPixel import SimPixel
from bibliopixel.drivers.spi_interfaces import SPI_INTERFACES
import string
import time

LED_LAYOUT = {
    'nest':[
    # Top panel
    [137, 138, 149, 150, 161, 162, 173, 174, 185, 186, 197],
    [136, 139, 148, 151, 160, 163, 172, 175, 184, 187, 196],
    [135, 140, 147, 152, 159, 164, 171, 176, 183, 188, 195],
    [134, 141, 146, 153, 158, 165, 170, 177, 182, 189, 194],
    [133, 142, 145, 154, 157, 166, 169, 178, 181, 190, 193],
    [132, 143, 144, 155, 156, 167, 168, 179, 180, 191, 192],
    # Middle panel
    [131, 120, 119, 108, 107, 96, 95, 84, 83, 72, 71],
    [130, 121, 118, 109, 106, 97, 94, 85, 82, 73, 70],
    [129, 122, 117, 110, 105, 98, 93, 86, 81, 74, 69],
    [128, 123, 116, 111, 104, 99, 92, 87, 80, 75, 68],
    [127, 124, 115, 112, 103, 100, 91, 88, 79, 76, 67],
    [126, 125, 114, 113, 102, 101, 90, 89, 78, 77, 66],
    # Bottom panel
    [5, 6, 17, 18, 29, 30, 41, 42, 53, 54, 65],
    [4, 7, 16, 19, 28, 31, 40, 43, 52, 55, 64],
    [3, 8, 15, 20, 27, 32, 39, 44, 51, 56, 63],
    [2, 9, 14, 21, 26, 33, 38, 45, 50, 57, 62],
    [1, 10, 13, 22, 25, 34, 37, 46, 49, 58, 61],
    [0, 11, 12, 23, 24, 35, 36, 47, 48, 59, 60]],
    
        'nest2': [
        # Top panel
        [197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187],
        [176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186],
        [175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165],
        [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164],
        [153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143],
        [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142],
        # Middle Panel
        [131, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121],
        [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
        [109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99],
        [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98],
        [87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77],
        [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76],
        # Bottom panel
        [65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55],
        [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
        [43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33],
        [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
        [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],

'evo': [[ 17,  18,  53,  54,  89,  90, 125, 126, 161, 162, 197],
       [ 16,  19,  52,  55,  88,  91, 124, 127, 160, 163, 196],
       [ 15,  20,  51,  56,  87,  92, 123, 128, 159, 164, 195],
       [ 14,  21,  50,  57,  86,  93, 122, 129, 158, 165, 194],
       [ 13,  22,  49,  58,  85,  94, 121, 130, 157, 166, 193],
       [ 12,  23,  48,  59,  84,  95, 120, 131, 156, 167, 192],
       [ 11,  24,  47,  60,  83,  96, 119, 132, 155, 168, 191],
       [ 10,  25,  46,  61,  82,  97, 118, 133, 154, 169, 190],
       [  9,  26,  45,  62,  81,  98, 117, 134, 153, 170, 189],
       [  8,  27,  44,  63,  80,  99, 116, 135, 152, 171, 188],
       [  7,  28,  43,  64,  79, 100, 115, 136, 151, 172, 187],
       [  6,  29,  42,  65,  78, 101, 114, 137, 150, 173, 186],
       [  5,  30,  41,  66,  77, 102, 113, 138, 149, 174, 185],
       [  4,  31,  40,  67,  76, 103, 112, 139, 148, 175, 184],
       [  3,  32,  39,  68,  75, 104, 111, 140, 147, 176, 183],
       [  2,  33,  38,  69,  74, 105, 110, 141, 146, 177, 182],
       [  1,  34,  37,  70,  73, 106, 109, 142, 145, 178, 181],
       [  0,  35,  36,  71,  72, 107, 108, 143, 144, 179, 180]]
}

no = (0, 0, 0)
gr = (20, 180, 20)
br = (70, 30, 30)
ye = (230, 230, 0)

TREE = [[no, no, no, no, no, ye, no, no, no, no, no],
        [no, no, no, no, ye, ye, ye, no, no, no, no],
        [no, no, no, no, no, ye, no, no, no, no, no],
        [no, no, no, no, no, gr, no, no, no, no, no],
        [no, no, no, no, gr, gr, gr, no, no, no, no],
        [no, no, no, gr, gr, gr, gr, gr, no, no, no],
        [no, no, no, no, gr, gr, gr, no, no, no, no],
        [no, no, no, gr, gr, gr, gr, gr, no, no, no],
        [no, no, gr, gr, gr, gr, gr, gr, gr, no, no],
        [no, no, no, gr, gr, gr, gr, gr, no, no, no],
        [no, no, gr, gr, gr, gr, gr, gr, gr, no, no],
        [no, gr, gr, gr, gr, gr, gr, gr, gr, gr, no],
        [no, no, gr, gr, gr, gr, gr, gr, gr, no, no],
        [no, gr, gr, gr, gr, gr, gr, gr, gr, gr, no],
        [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
        [no, no, no, no, br, br, br, no, no, no, no],
        [no, no, no, no, br, br, br, no, no, no, no],
        [no, no, no, no, br, br, br, no, no, no, no], ]

class MoonBoard:
    DEFAULT_PROBLEM_COLORS = {'START':COLORS.green,'TOP':COLORS.red,'MOVES':COLORS.blue}
    DEFAULT_COLOR = COLORS.blue
    X_GRID_NAMES = string.ascii_uppercase[0:11]
    NUM_PIXELS = 198
    DEFAULT_BRIGHTNESS = 200

    def __init__(self, driver_type, led_layout=None, brightness=DEFAULT_BRIGHTNESS):
        try:
            if driver_type == "PiWS281X":
                driver = PiWS281X(self.NUM_PIXELS, c_order = "rgb")
            elif driver_type == "WS2801":
                driver = WS2801(self.NUM_PIXELS, dev='/dev/spidev0.1',spi_interface= SPI_INTERFACES.PERIPHERY,spi_speed=1)
            elif driver_type == "SimPixel":
                driver = SimPixel(self.NUM_PIXELS)
                driver.open_browser()
            else:
                raise ValueError("driver_type {driver_type} unknow.".format(driver_type) )
        except (ImportError, ValueError) as e:
            print("Not able to initialize the driver. Error{}".format(e))
            print("Use bibliopixel.drivers.dummy_driver")
            driver = DriverDummy(self.NUM_PIXELS)

        if led_layout is not None:
            self.layout = Matrix(driver,
                                width=11,
                                height=18,
                                coord_map=led_layout,
                                threadedUpdate=True,
                                brightness=brightness
                                )
        else:
            self.layout = Matrix(driver,width=11,height=18, 
                                threadedUpdate=True,
                                brightness=brightness
                                )
        self.layout.cleanup_drivers()
        self.layout.start()
        self.animation = None

    def clear(self):
        self.stop_animation()
        self.layout.all_off()
        self.layout.push_to_driver()

    def set_hold(self, hold, color=DEFAULT_COLOR):
        x_grid_name, y_grid_name = hold[0], int(hold[1:])
        x = self.X_GRID_NAMES.index(x_grid_name)
        y = 18 - y_grid_name
        self.layout.set(x, y, color)

    def show_hold(self, hold, color=DEFAULT_COLOR):
        self.set_hold(hold, color)
        self.layout.push_to_driver()
        
    def set_hold_row(self, row, hold, color=DEFAULT_COLOR):
        x_grid_name, y_grid_name = hold[0], int(hold[1:])
        x = self.X_GRID_NAMES.index(x_grid_name)
        y = 18 - y_grid_name
        if y == row:
            self.layout.set(x, y, color)

    def show_problem(self, holds, hold_colors={}):
        self.clear()
        for k in ['START', 'MOVES', 'TOP']:
            for hold in holds[k]:
                self.set_hold(
                    hold, 
                    hold_colors.get(k, self.DEFAULT_PROBLEM_COLORS[k]),
                    )
        self.layout.push_to_driver()
        
    def animate_problem(self, holds, hold_colors={}):
        last_x = -1
        def setLED(x,y, val):
            if (y >=0):
                self.layout.set(x, y, val)

        for i in range(0, 22):
            for p in range(11):
                setLED(p, i - 3, (0, 0, 0))
                setLED(p, i - 2, (0, 0, 50))
                setLED(p, i - 1, (0, 0, 150))
                setLED(p, i, (0, 0, 250))

            for k in ['START', 'MOVES', 'TOP']:
                for hold in holds[k]:
                    self.set_hold_row(i - 1,
                                      hold,
                                      hold_colors.get(k, self.DEFAULT_PROBLEM_COLORS[k]), )
                    self.set_hold_row(i - 2,
                                      hold,
                                      hold_colors.get(k, self.DEFAULT_PROBLEM_COLORS[k]), )
                    self.set_hold_row(i - 3,
                                      hold,
                                      hold_colors.get(k, self.DEFAULT_PROBLEM_COLORS[k]), )

            self.layout.push_to_driver()
            time.sleep(0.01)
            
    # def animate_tree(self):
    #     for n in range(18):
    #         for y in range(n + 1):
    #             for x in range(11):
    #                 self.layout.set(x, 17 - n + y, TREE[y][x])

    #         self.layout.push_to_driver()
    #         time.sleep(.15)
            
    def animate_tree(self):
        frametime = 0.02
        itermpolate = 3
        for n in range(18):
            for m in range(itermpolate):
                for y in range(n + 1):
                    if y<18:
                        for x in range(11):
                            base = TREE[y-1][x]
                            tar = TREE[y][x]
                            diff = [(t - b)/itermpolate for b, t in zip(base, tar)]
                            
                            # addvalue = (TREE[y][x] - TREE[y-1][x])/itermpolate
                            self.layout.set(x, 17 - n + y, [(int(b + d * m)) for b, d in zip(base, diff)])
                            # self.layout.set(x, 17 - n + y, list(base + addvalue * m))
                self.layout.push_to_driver()
                time.sleep(frametime)

            for y in range(n + 1):
                for x in range(11):
                    self.layout.set(x, 17 - n + y, list(TREE[y][x]))

            self.layout.push_to_driver()
            time.sleep(frametime)

    def run_animation(self, animation, run_options={}, **kwds):
        self.stop_animation()
        self.animation = animation(self.layout, **kwds)
        self.animation.run(**run_options)

    def stop_animation(self):
        if self.animation is not None:
            self.animation.stop()


class TestAnimation:
    COLOR=[COLORS.Green, COLORS.Blue]
    def __init__(self, layout, ):
        self.layout = layout

    def step(self, amt=1):
        pass

if __name__=="__main__":
    import argparse
    import time
    import subprocess

    parser = argparse.ArgumentParser(description='Test led system')

    parser.add_argument('driver_type', type=str,
                        help='driver type, depends on leds and device controlling the led.',choices=['PiWS281X', 'WS2801', 'SimPixel'])
    parser.add_argument('--duration',  type=int, default=10,
                        help='Delay of progress.')
    parser.add_argument('--special_nest_layout',  action='store_true')
    args = parser.parse_args()
    
    print("Test MOONBOARD LEDS\n===========")
    led_layout = LED_LAYOUT['nest'] if args.special_nest_layout else None
    MOONBOARD = MoonBoard(args.driver_type,led_layout )
    print("Run animation,")
    #animation=
    #MoonBoard.run_animation()
    #MOONBOARD.layout.fillScreen(COLORS.red)
    #print(f"wait {args.duration} seconds,")
    time.sleep(args.duration)
    print("clear and exit.")
    MOONBOARD.clear()