print("Starting")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kb import data_pin
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.hid import HIDModes

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP10,board.GP16,board.GP14,board.GP15)
keyboard.row_pins = (board.GP4,board.GP5,board.GP6,board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

i2c_bus = busio.I2C(board.GP2, board.GP3)
display_driver = SSD1306(
    i2c=i2c_bus,
       device_address=0x3C,
)

def connetion():
    if keyboard.hid_helper.ble.connected:
        return "Connected"
    else :
        return "Disconnected"

display = Display(
    display=display_driver,
    entries = [
    TextEntry(text="@Fallout_Shenzhen", x=128, y=0, x_anchor="R", y_anchor="T"), 
    TextEntry(text=connetion(), x=0, y=0, x_anchor="L", y_anchor="T"),
    ImageEntry(image="D:\Nonwire_keyboad\Nonwire_keyboard\Firmware\vert_cat.bmp", x=0, y=0),
    ],
    height=64,
    off_time=1200,
    brightness=0.5,
    brightness_step=0.2,
)

keyboard.extensions.append(display)
keyboard.keymap = [
    [KC.NLCK,KC.PSLS,KC.PAST,KC.PMNS,
     KC.P7,KC.P8,KC.P9,KC.PPLS,
     KC.P4,KC.P5,KC.P6,
     KC.P1,KC.P2,KC.P3,KC.PENT,
     KC.P0,KC.PDOT
     ]
]

split = Split(split_type=SplitType.BLE, split_side=SplitSide.RIGHT)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='Numpad')