import machine
import utime

#LED Lights
onboard_led = machine.Pin(25, machine.Pin.OUT)
led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
led_green2 = machine.Pin(12, machine.Pin.OUT)
led_red2 = machine.Pin(11, machine.Pin.OUT)

#switch
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

#buzzer
buzzer = machine.Pin(12, machine.Pin.OUT)

while True:
    if button.value() == 1:
        onboard_led.value(1)
        led_green.value(1)
        buzzer.value(1)

    else:
        onboard_led.value(0)
        led_green.value(0)
        buzzer.value(0)
  
    
    
   
  