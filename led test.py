import machine
import utime

led = machine.Pin(1, machine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(1)