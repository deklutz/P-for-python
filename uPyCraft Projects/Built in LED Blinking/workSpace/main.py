from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(19, Pin.OUT)

while True:
  led.value (not led.value())
  sleep (0.1)
  led2.value (not led2.value())
  sleep (0.3)
  led3.value (not led3.value())
  sleep (0.5)
