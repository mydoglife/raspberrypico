import machine
import utime

potentiometer = machine.ADC(28)
servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    #print("Duty " + str(duty))
    pin.duty_u16(duty)
    #print(pin.duty_u16())

while True:
    #value=potentiometer.read_u16()
    user_angle = int(input("Type in angle 0 to 180: "))
    #user_angle = int(user_angle)
    
    #angle=interval_mapping(user_angle,0,65535,0,180)  
    servo_write(servo,user_angle)

    utime.sleep_ms(200)
    

