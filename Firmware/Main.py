print("Starting")

import board
import busio 

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kb import data_pin
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.hid import HIDModes

keyboard = KMKKeyboard()
layers_module = Layers()
keyboard.modules.append(layers_module)
keyboard.col_pins = (board.GP7,board.GP8,board.GP9,board.GP10,board.GP16,board.GP14,board.GP15,board.GP18,board.GP19,board.GP20,board.GP21,board.GP25,board.GP26,board.GP27)
keyboard.row_pins = (board.GP1,board.GP2,board.GP4,board.GP5,board.GP6)
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
    TextEntry(text="@Youssef", x=128, y=0, x_anchor="R", y_anchor="T"), 
    TextEntry(text=connetion(), x=0, y=0, x_anchor="L", y_anchor="T"),
    ImageEntry(image="D:\Nonwire_keyboad\Nonwire_keyboard\Firmware\vert_cat.bmp", x=0, y=0),
    ],
    height=64,
    off_time=1200,
    brightness=0.5,
    brightness_step=0.2,
    dim_time=500,
     dim_target=0.1
)
FN = KC.MO(1)
keyboard.keymap = [
    # layer 0
    [KC.ESC,KC.GRV,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.MINS,KC.EQL,
     KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.LBRC,KC.RBRC,KC.BSPC,
     KC.CAPS,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCLN,KC.QUOT,KC.ENT,KC.BSLS,
     KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,KC.SLSH,KC.RSFT,KC.P8,
     KC.LCTL,KC.LWIN,KC.LALT,KC.SPC,KC.RALT,FN,KC.RCTL,KC.P4,KC.P2,KC.P6

     ]
    # layer 1
    [
        KC.TRNS,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.TRNS,KC.TRNS,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS
    ]
]
split = Split(split_type=SplitType.BLE, split_side=SplitSide.LEFT,split_target_left=True)
keyboard.modules.append(split)

if __name__ == '__main__':
        keyboard.go(hid_type=HIDModes.BLE, ble_name='Youssef_Keyboard')