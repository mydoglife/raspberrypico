#An alarm clock with Raspberry Pico
#2 line LCD Screen
#Tells current time
#Tells the alarm time that's set
#Adjusts current time, Hour and Minute
#Adjusts alarm time, Hour and Minute
#Button to turn alarm off

import machine
import utime
from pico_i2c_lcd import I2cLcd
import utime as time

#CONSTANTS
I2C_ADDR = 0x27 #39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
 
#setup LCD
i2c = machine.I2C(id=0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
 
#set up buttons
hour_button = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)    #green button
minute_button = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN) #blue button
alarm_off_button = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN) #red alarm off button

#switches
alarm_set_switch = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN) #top slide switch
clock_set_switch = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)   #bottom slide switch


#led lights
alarm_led_red = machine.Pin(14, machine.Pin.OUT)
hour_led_green = machine.Pin(12, machine.Pin.OUT)
minute_led_blue = machine.Pin(13, machine.Pin.OUT)

#passive buzzer
buzzer = machine.PWM(machine.Pin(20))

#ode to joy
C_NOTE = 262
D_NOTE = 294
E_NOTE = 330
F_NOTE = 349
G_NOTE = 392

melody = [E_NOTE, E_NOTE, F_NOTE, G_NOTE, G_NOTE, F_NOTE, E_NOTE, D_NOTE, C_NOTE, C_NOTE, D_NOTE, E_NOTE, D_NOTE, D_NOTE]

#testing buttons and buzzer
def tone(pin, frequency, duration):
    pin.freq(frequency)
    pin.duty_u16(30000)
    utime.sleep_ms(duration)
    pin.duty_u16(0)

def play_melody():
    for note in melody:
        tone(buzzer,note,400)
        utime.sleep_ms(150)


#Variables
#clock variables
current_hour = 0
current_minute = 0
clock_AMPM = "AM"
hour_interval = 0
minute_interval = 0

#alarm variables
alarm= utime.localtime() #just setting it so I start from zero in the same format as time
alarm_hour = int(alarm[3])
alarm_minute = int(alarm[4])
alarm_second = 0 #is always zero!!!
alarm_set = True
alarm_AMPM = "AM"
display_alarm_hour = 0
alarm_off = False
set_alarm = False
alarm_on = True

#handle alarm off button
def alarm_off_handler(): 
    global alarm_on
    if alarm_on:
        alarm_on = False

def alarm_setting_handler():
    global set_alarm
    set_alarm = True
    while set_alarm:
        if hour_button.value() == 1:
            global alarm_hour
            alarm_hour = alarm_hour+1
            lcd.putstr("Time: ")
            lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=current_hour, MM=time[4], SS=time[5]) + clock_AMPM)
        if minute_button.value() == 1:
            global alarm_minute
            alarm_minute = alarm_minute +1           

def clock_set_handler():
    global set_clock
    set_clock = True
    while set_clock:
        if hour_button.value() == 1:
            global current_hour
            current_hour = current_hour + 1
        if minute_button.value() == 1:
            global current_minute
            current_minute = current_minute + 1
    return hour_adjust, minute_adjust #returns tuple, not is not changeable!!!


def display_clock(current_hour, current_minute, current_second, clock_AMPM,lcd):
    lcd.clear()
    lcd.move_to(0,0)
    if int(current_hour) > 12:
        current_hour = int(current_hour)-12  
        clock_AMPM = "PM"
    elif int(current_hour) == 0:
        current_hour = 12
        clock_AMPM = "AM"
    else:
        current_hour = int(current_hour)
#print the current time            
    lcd.putstr("Time: ")
    lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=current_hour, MM=current_minute, SS=current_second) + clock_AMPM)
    
def display_alarm(alarm_hour, alarm_minute, alarm_second, alarm_AMPM, lcd, alarm_set):
       lcd.move_to(0,1)
       if alarm_set:
        if alarm_hour > 12:
            alarm_hour = alarm_hour - 12  
            alarm_AMPM = "PM"
        elif int(alarm_hour) == 0:
            display_alarm_hour = 12
            alarm_AMPM = "AM"
        lcd.putstr("Alarm:")
        lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=alarm_hour, MM=alarm_minute, SS=alarm_second)+alarm_AMPM)
        
clock_set_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=clock_set_handler)
alarm_off_button.irq(trigger=machine.Pin.IRQ_RISING, handler=alarm_off_handler)
alarm_set_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=alarm_setting_handler)

while True:       
    time = utime.localtime() #real current time - might have to move it if off computer
    current_hour = int(time[3])
    current_minute = int(time[4])
    current_second = int(time[5])
  
    if alarm_hour == current_hour and alarm_minute == current_minute and alarm_second == current_second and alarm_set==True:
        alarm_on = True
        while alarm_on:
            buzzer.toggle()
            utime.sleep_ms(100)
         
    display_clock(current_hour, current_minute, current_second, clock_AMPM, lcd)
    display_alarm(alarm_hour, alarm_minute, alarm_second, alarm_AMPM, lcd, alarm_set)            
    utime.sleep(1)           
            
# #printing the current time and alarm
#     lcd.clear()
#     if int(time[3]) > 12:
#         current_hour = int(time[3])-12  
#         clock_AMPM = "PM"
#     elif int(time[3]) == 0:
#         current_hour = 12
#         clock_AMPM = "AM"
#     else:
#         current_hour = int(time[3])
# #print the current time            
#     lcd.putstr("Time: ")
#     lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=current_hour, MM=time[4], SS=time[5]) + clock_AMPM)
#checking to see if alarm is on or not 
#     if alarm_set:
#         if alarm_hour > 12:
#             display_alarm_hour = alarm_hour - 12  #don't want to mess with "actual" alarm_hour
#             alarm_AMPM = "PM"
#         elif int(alarm_hour) == 0:
#             display_alarm_hour = 12
#             alarm_AMPM = "AM"
#         lcd.putstr("Alarm:")
#         lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=display_alarm_hour, MM=alarm_minute, SS=alarm_second)+alarm_AMPM)
#     utime.sleep(1)


   
