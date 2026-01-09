from machine import Pin, time_pulse_us
import time

# Ultrasonic pins
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

# LEDs (Street Light Poles)
led1 = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)
led3 = Pin(16, Pin.OUT)
led4 = Pin(17, Pin.OUT)

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

    # Turn OFF all lights first
    led1.off()
    led2.off()
    led3.off()
    led4.off()

    if 0 < dist <= 10:
        led1.on()
    elif dist <= 20:
        led2.on()
    elif dist <= 30:
        led3.on()
    elif dist <= 40:
        led4.on()

    time.sleep(0.5)
