from machine import Pin, PWM, time_pulse_us
import time

# Pin setup
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)
led = Pin(2, Pin.OUT)

# Passive buzzer module (PWM)
buzzer = PWM(Pin(15))
buzzer.duty(0)
buzzer.freq(2000)

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

def buzzer_on():
    buzzer.duty(512)

def buzzer_off():
    buzzer.duty(0)

while True:
    dist = get_distance()
    print("Distance:", dist, "cm")

    if 0 < dist < 20:
        led.on()
        buzzer_on()
    else:
        led.off()
        buzzer_off()

    time.sleep(0.5)
