from machine import Pin
import utime

relay = Pin(18, Pin.OUT)
led = Pin(25, Pin.OUT)

# Initialize: led and circuite closed
relay(1)
led.value(1)

while True:
    utime.sleep(86400)
 
    # Turn off and back on again
    relay(0)
    led.value(0)
    print('turn circuit off')
 
    utime.sleep(0.5)
    relay(1)
    led.value(1)
    print('turn circuit back on')
