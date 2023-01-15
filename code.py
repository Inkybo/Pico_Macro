print("Starting")

import board
import busio as io


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode
from kmk.modules.encoder import EncoderHandler

#OLED imports
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
keyboard = KMKKeyboard()
keyboard.extensions.append(oled_ext)


keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()


keyboard.row_pins = (board.GP8, board.GP9)    # try D6 on Feather, keeboar
keyboard.col_pins = (board.GP4, board.GP5, board.GP6, board.GP7)    # try D5 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.ROW2COL

i2c = io.I2C(scl=board.GP11, sda=board.GP10)
trackball = Trackball(i2c)
keyboard.modules.append(trackball)

r = 96
g = 50
b = 14
w = 0
brightness = 255

trackball.set_rgbw(r, g, b, w)
#trackball.set_red(brightness)
#trackball.set_green(brightness)
#trackball.set_blue(brightness)
#trackball.set_white(brightness)

#USEFUL KEYS
XXXXXXX = KC.NO #ignore key (NOOP)

keyboard.keymap = [
    [
        XXXXXXX,	KC.HYPER,	KC.MEH,	KC.LGUI,
        XXXXXXX,	KC.F,	KC.G,	KC.H
    ]
]

if __name__ == '__main__':
    keyboard.go()
