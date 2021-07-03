import machine
import time

data = machine.Pin(0,machine.Pin.OUT)
latch = machine.Pin(1,machine.Pin.OUT) #rclk
clock = machine.Pin(2,machine.Pin.OUT) #srclk

def shift_update(input,data,clock,latch):
  #put latch down to start data sending
    clock.low()
    latch.low()
    clock.high()

  #load data in reverse order
    for i in range(7, -1, -1):
        clock.low()
        data.value(int(input[i]))
        clock.high()

  #put latch up to store data on register
    clock.low()
    latch.high()
    clock.high()

while True:
    n=int(input('please enter the no. in decimal format (0 to 255): '))
    user_input=n #temperary variable to iterate thru user_input
    k=[] #array to store binary number

    for z in range(8):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
        print(k) #to show how it's iterating thru the 8 bits of the binary
    
    string="" #setting string to nothing at first

#I need to convert the binary number into a string, so we can index it for the lights
    for j in k[::-1]:
        string=string+str(j)
    print('The binary no. for %d is %s'%(user_input, string))
    
    shift_update(string, data, clock, latch) #writing it out to the leds