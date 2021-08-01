from machine import UART,Pin
rxData = bytes()
uart1 = UART(0,baudrate=9600,tx=Pin(0),rx=Pin(1))
relay = Pin(3,Pin.OUT)
relay.value(0)
uart1.write("Starting Application\r\n")
while True:
    if uart1.any() > 0:
        rxData = uart1.read(1);
        if "1" in rxData:
            uart1.write("Turning ON\r\n")
            print("Turning ON\r\n")
            relay.value(1)
        elif "0" in rxData:
            uart1.write("Turning OFF\r\n")
            print("Turning OFF\r\n")
            relay.value(0)