import machine

pwm = machine.PWM(machine.Pin(12))
pwm.freq(50)

# create a PWM object on a pin
pwm.duty_u16(32768)     # set duty to 50%
# reinitialise with a period of 200us, duty of 5us

pwm.duty_ns(3000)       # set pulse width to 3us
pwm.deinit()