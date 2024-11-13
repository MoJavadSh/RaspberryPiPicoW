import network
import socket
from machine import Pin
import time

red_led = Pin(15, Pin.OUT)
blue_led = Pin(16, Pin.OUT)
led = Pin("LED", Pin.OUT)

#Wifi configuration
ssid = 'SSID-Name'       
password = 'Password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

  # Connecting to Wifi with LED blinks
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)


if wlan.status() != 3:
    for i in range (10):
        led.value(1)
        time.sleep(0.02)
        led.value(0)
        time.sleep(0.02)

    raise RuntimeError('network connection failed')
    
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    led.value(1)
    time.sleep(5)



# HTML
html = """<!DOCTYPE html>
<html>
<head>
    <title>LED</title>
</head>
<body>
    <h1>Control LEDs</h1>
    <form action="/blue_on" method="POST">
        <input type="submit" value="Turn Blue LED ON">
    </form>
    <form action="/blue_off" method="POST">
        <input type="submit" value="Turn Blue LED OFF">
    </form>
    <form action="/red_on" method="POST">
        <input type="submit" value="Turn Red LED ON">
    </form>
    <form action="/red_off" method="POST">
        <input type="submit" value="Turn Red LED OFF">
    </form>
</body>
</html>
"""

#Simple web server
def web_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    
    print('Listening on', addr)
    
    while True:
        client, addr = s.accept()
        print('Client connected from', addr)
        request = client.recv(1024).decode()
        print(request)

        #Control LEDs 
        if 'POST /blue_on' in request:
            blue_led.on()
        elif 'POST /blue_off' in request:
            blue_led.off()
        elif 'POST /red_on' in request:
            red_led.on()
        elif 'POST /red_off' in request:
            red_led.off()

        #HTML response
        client.send('HTTP/1.1 200 OK\n')
        client.send('Content-Type: text/html\n')
        client.send('Connection: close\n\n')
        client.sendall(html)
        client.close()


web_server()
