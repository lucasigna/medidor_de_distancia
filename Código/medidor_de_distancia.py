from machine import Pin
from time import sleep
import utime
from lcd1602 import LCD1602
from hcsr04 import HCSR04

# Setup
rs = Pin(22, Pin.OUT)
e = Pin(23, Pin.OUT)
d4 = Pin(17, Pin.OUT)
d5 = Pin(18, Pin.OUT)
d6 = Pin(19, Pin.OUT)
d7 = Pin(21, Pin.OUT)

# Instancio la clase para el sensor ultrasónico
sensor = HCSR04(trigger_pin=15, echo_pin=16, echo_timeout_us=10000)

# Instancio la clase para el LCD
lcd = LCD1602(rs=22, e=23, d4=17, d5=18, d6=19, d7=21)
lcd.init()

while True:
    distance = sensor.distance_cm()
    if distance < 0:
        lcd.write("Error",1)
        continue
    lcd.write('Distancia:', 1)
    lcd.write( str(round(distance,1)) + ' cm', 2)
    sleep(1)
    lcd.clear()