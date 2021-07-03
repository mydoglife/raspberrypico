from pico_i2c_lcd import I2cLcd
from machine import I2C
from machine import Pin
import utime as time
 
 
i2c = I2C(id=0,sda=Pin(0),scl=Pin(1),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
 
while True:
      lcd.move_to(2,0)
      lcd.putstr('Hello world')
      lcd.move_to(2,1)
      lcd.putstr('You suck!')