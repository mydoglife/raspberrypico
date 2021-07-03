import time
import board
from digitalio import DigitalInOut, Direction, Pull
import time
import usb_hid
from adafruit_hid.mouse import Mouse
 
mouse = Mouse(usb_hid.devices)

print("prepare you mouse - place it over plate")

for y in range(5,0, -1):
    time.sleep(1)
    print(y)

for x in range(1000):
    mouse.press(Mouse.LEFT_BUTTON)
    mouse.release(Mouse.LEFT_BUTTON) #remember, if it presses, it needs a release
    print(x, "clicks")
