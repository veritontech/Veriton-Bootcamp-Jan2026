from machine import Pin, time_pulse_us
import time

# Ultrasonic pins
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

# LEDs
green = Pin(2, Pin.OUT)
yellow = Pin(4, Pin.OUT)
red = Pin(16, Pin.OUT)

def get_distance():
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0:
        return -1

    distance = (duration * 0.0343) / 2
    return distance

while True:
    dist = get_distance()
    print("Distance:", dist, "cm")

    # Turn OFF all LEDs
    green.off()
    yellow.off()
    red.off()

    if dist > 60:
        green.on()      # Slot Free
    elif dist > 30:
        yellow.on()     # Slot Almost Full
    elif dist > 0:
        red.on()        # Slot Full

    time.sleep(0.5)
