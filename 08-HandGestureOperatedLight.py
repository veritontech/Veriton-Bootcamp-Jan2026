import network
import socket
from machine import Pin
import time
# ==============================
# LED PINS
# ==============================
leds = {
    "thumb":  Pin(27, Pin.OUT),
    "index":  Pin(26, Pin.OUT),
    "middle": Pin(25, Pin.OUT),
    "ring":   Pin(14, Pin.OUT),
    "pinky":  Pin(13, Pin.OUT)
}
# LEDs ON initially (because logic is reversed)
for led in leds.values():
    led.on()
# ==============================
# WIFI SETUP
# ==============================
SSID = "Your_Wifi_Name"
PASSWORD = "Your_Wifi_Password"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)
while not wifi.isconnected():
    time.sleep(0.5)
print("WiFi Connected")
print("ESP32 IP:", wifi.ifconfig()[0])
# ==============================
# SIMPLE WEB SERVER (NO HTML)
# ==============================
server = socket.socket()
server.bind(("", 80))
server.listen(5)
# ==============================
# LED CONTROL FUNCTION (REVERSED)
# ==============================
def control_led(name, state):
    if name in leds:
        if state == "on":
            leds[name].off()   # REVERSED
        elif state == "off":
            leds[name].on()    # REVERSED
        print(name.upper(), state.upper(), "(REVERSED)")
# ==============================
# MAIN LOOP
# ==============================
while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode()
    # Example URL: /led/thumb/on
    if "/led/" in request:
        try:
            path = request.split(" ")[1]
            _, _, name, state = path.split("/")
            control_led(name, state)
        except:
            pass
    conn.send("HTTP/1.1 200 OK\n\nOK")
    conn.close()
