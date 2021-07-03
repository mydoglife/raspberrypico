import machine
from ws2812 import WS2812
import utime
import urandom

ws = WS2812(machine.Pin(0),8)

def flowing_light():
    for i in range(7,0,-1):
        ws[i] = ws[i-1]
        print(i)
        #print(i-1)
    ws[0] = int(urandom.uniform(0, 0xFFFFFF))
    ws.write()
    utime.sleep_ms(500)

while True:
    flowing_light()
    ws.write() 
    #print(ws[0])
