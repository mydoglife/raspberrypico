import machine
import time

SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

sdi = machine.Pin(0,machine.Pin.OUT) #data
rclk = machine.Pin(1,machine.Pin.OUT) #latch
srclk = machine.Pin(2,machine.Pin.OUT) #clock

def hc595_shift(dat):
    rclk.low()          #turning latch to zero
    time.sleep_ms(5)
    for bit in range(7, -1, -1):
        srclk.low()      #turning clock to zero
        time.sleep_ms(5)
        value = 1 & (dat >> bit) #bitwise operator - shifts bits to the right, shifts dat to right by bit
        sdi.value(value)
        time.sleep_ms(5)
        srclk.high()       #turning clock to 1
#         time.sleep_ms(5)
    time.sleep_ms(5)
    rclk.high()             #turning latch to 1 to move it into memory
#     time.sleep_ms(5)
    
while True:
    for num in range(10):
        hc595_shift(SEGCODE[num])
        time.sleep_ms(500)
    
    hc595_shift(0xF3)
    time.sleep_ms(500)
    hc595_shift(0x80)
    time.sleep_ms(500)
