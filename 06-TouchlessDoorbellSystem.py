from machine import Pin, PWM
import time

# IR sensor pin
ir = Pin(21, Pin.IN)

# Passive buzzer (PWM)
buzzer = PWM(Pin(15))
buzzer.freq(2000)
buzzer.duty(0)

while True:
    if ir.value() == 1:
        buzzer.duty(512)   # Bell ON
    else:
        buzzer.duty(0)     # Bell OFF

    time.sleep(0.1)
