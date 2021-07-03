import utime
from servo import Servo

s1 = Servo(15)       # initialize servo on GPIO pin 0

while True:
    s1.goto(0)      # move arm all the way to one side
    utime.sleep(1)
    s1.goto(1024)   # move arm all the way to the other side
    utime.sleep(1)
    s1.goto(512)
    utime.sleep(1)