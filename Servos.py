from machine import Pin, PWM
import utime

MID = 1500000  #1.5ms
MIN = 1000000  #1ms
MAX = 2000000  #2ms
TEST = 900000

led = Pin(25, Pin.OUT)
pwm = PWM(Pin(15))

pwm.freq(50) #hertz
pwm.duty_ns(MID)

while True:
    pwm.duty_ns(MIN)  #in nanoseconds
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1)
    pwm.duty_ns(MAX)
    utime.sleep(1)
    pwm.duty_ns(TEST)
    utime.sleep(1)
    
