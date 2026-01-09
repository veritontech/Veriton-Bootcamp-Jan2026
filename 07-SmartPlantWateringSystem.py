from machine import Pin
import time

# LDR digital output
ldr = Pin(4, Pin.IN)

# Relay pin
relay = Pin(23, Pin.OUT)
relay.off()   # Pump OFF initially

while True:
    light = ldr.value()

    if light == 1:
        # Bright light detected (day time)
        relay.on()      # Pump ON
    else:
        # Low light (night time)
        relay.off()     # Pump OFF

    time.sleep(1)
