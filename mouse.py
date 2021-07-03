import time
import board
from digitalio import DigitalInOut, Direction, Pull
import time
import usb_hid
from adafruit_hid.mouse import Mouse
 
mouse = Mouse(usb_hid.devices)

for z in range(10):
    x=130
    y=130
    mouse.move(x,y)
    time.sleep(.5)
    x=-130
    y=-130
    mouse.move(x,y)
    time.sleep(.5)

# This will move the mouse from its current position to x pixels 
# and y pixels. 
# So if the current position is (100,200) it'll move to
# (100+x,100+y)

