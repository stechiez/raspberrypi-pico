from machine import Pin
import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import math
import utime

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

sda=machine.Pin(4)
scl=machine.Pin(5)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
#  print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c)
oled.text("STechiezDIY !!!",5,5)
oled.text("Pico",5,15)
oled.text("HCSR04",5,25)
oled.text("SSD1306",5,35)
trigger = Pin(14, Pin.OUT)
echo = Pin(13, Pin.IN)
def get_distance():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
   return distance
while True:
   oled.fill(0)   
   ret_val = get_distance()
   oled.text("Distance:",0,0)
   oled.text(str(ret_val) + " cm",0,10)
   oled.show()
   utime.sleep(1)
