import time
from machine import Pin

bargraph_led0 = Pin(9,Pin.OUT)
bargraph_led1 = Pin(8,Pin.OUT)
bargraph_led2 = Pin(7,Pin.OUT)
bargraph_led3 = Pin(6,Pin.OUT)
bargraph_led4 = Pin(13,Pin.OUT)
bargraph_led5 = Pin(12,Pin.OUT)
bargraph_led6 = Pin(11,Pin.OUT)
bargraph_led7 = Pin(10,Pin.OUT)
bargraph_value = 0

def bargraph(display_data):
    bargraph_led0.value(1 if display_data&0x01 else 0)
    bargraph_led1.value(1 if display_data&0x02 else 0)
    bargraph_led2.value(1 if display_data&0x04 else 0)
    bargraph_led3.value(1 if display_data&0x08 else 0)
    bargraph_led4.value(1 if display_data&0x10 else 0)
    bargraph_led5.value(1 if display_data&0x20 else 0)
    bargraph_led6.value(1 if display_data&0x40 else 0)
    bargraph_led7.value(1 if display_data&0x80 else 0)
    time.sleep(1)    
    

while True:
    bargraph_value = 0
    bargraph(bargraph_value)
    
    for x in range (0,8):
        bargraph_value |= (1 << x);
        bargraph(bargraph_value)
        print(hex(bargraph_value))
    
