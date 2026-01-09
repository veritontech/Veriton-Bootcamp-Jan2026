from machine import Pin
import time

# LDR digital output pin
ldr = Pin(4, Pin.IN)

# LED pin
led = Pin(2, Pin.OUT)

while True:
    light_status = ldr.value()

    if light_status == 0:
        # Andhera hai
        led.on()
    else:
        # Roshni hai
        led.off()

    time.sleep(0.5)
