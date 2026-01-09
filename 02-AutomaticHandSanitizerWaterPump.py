#01. Load/Import Library
from machine import Pin, PWM
import time

#02. IR sensor pin
ir = Pin(21, Pin.IN)

#03. Passive buzzer (PWM)
buzzer = PWM(Pin(15))
buzzer.freq(2000)
buzzer.duty(0)

#04. Listen and respond to IR sensor
while True:
    if ir.value() == 1:
        buzzer.duty(512)   # Bell ON
    else:
        buzzer.duty(0)     # Bell OFF

    time.sleep(0.1)
