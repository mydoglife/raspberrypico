import machine
import utime

#A = 440, B= 493.88, C# = 554.37, D = 587.33, E = 659.25     

Anote = 440
Bnote = 494
Csharpnote = 554
Dnote = 587
Enote = 659

buzzer = machine.PWM(machine.Pin(15))

button_A= machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_B= machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_C= machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_D= machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_E= machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)

def tone(pin,frequency,duration):
    pin.freq(frequency)
    pin.duty_u16(30000)
    utime.sleep_ms(duration)
    pin.duty_u16(0)

while True:
    if button_A.value() == 1: 
        tone(buzzer,Anote,250)
        utime.sleep_ms(250)
    elif button_B.value() == 1:
        tone(buzzer,Bnote,250)
        utime.sleep_ms(250)
    elif button_C.value() == 1:
        tone(buzzer,Csharpnote,250)
        utime.sleep_ms(250)
    elif button_D.value() == 1:
        tone(buzzer,Dnote,250)
        utime.sleep_ms(250)
    elif button_E.value() == 1:
        tone(buzzer,Enote,250)
        utime.sleep_ms(250)
    else:
        utime.sleep_ms(250)
        
        
        
