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
html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>LED</title>
    <link rel="stylesheet" href="styles.css" />
    <style>
      /* General styles */
      body {
        margin: 0;
        font-family: Arial, sans-serif;
        background-color: #121212; /* Dark background */
        color: #f5f5f5; /* Light text color */
      }

      header {
        text-align: center;
        padding: 20px;
        background-color: #1f1f1f;
        border-bottom: 2px solid #333;
      }

      h1 {
        font-size: 2rem;
        margin: 0;
      }

      main {
        display: flex;
        justify-content: center;
        padding: 20px;
      }

      .container {
        display: flex;
        flex-direction: row;
        gap: 20px; /* Space between the two sections */
      }

      .section {
        display: flex;
        flex-direction: column;
        gap: 20px; /* Space between each part */
        background-color: #b2f0e3;
        padding: 20px;
        border-radius: 10px;
        width: 100%;
        max-width: 400px;
      }

      .part {
        text-align: center;
        padding: 20px;
        border: 1px solid #333;
        background-color: #f5f5f5;
        color: #121212;
        border-radius: 10px;
      }

      /* Red buttons for section 1 */
      #button1,
      #button2 {
        padding: 20px;
        font-size: 1.2rem;
        background-color: red;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
      }

      /* Blue buttons for section 2 */
      #button3,
      #button4 {
        padding: 20px;
        font-size: 1.2rem;
        background-color: blue;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
      }

      button:hover {
        opacity: 0.8;
      }

      footer {
        text-align: center;
        padding: 20px;
        background-color: #1f1f1f;
        border-top: 2px solid #333;
      }

      /* Responsive design */
      @media (max-width: 768px) {
        .container {
          flex-direction: column;
          align-items: center;
        }

        .section {
          max-width: 100%;
          width: 100%;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Responsive Interactive Web Page</h1>
    </header>

    <main>
      <div class="container">
        <!-- First vertical section -->
        <div class="section">
          <div class="part">
            <form action="/red_on" method="POST">
              <button id="button1">Button 1</button>
            </form>
          </div>
          <div class="part">
            <form action="/red_off" method="POST">
              <button id="button2">Button 2</button>
            </form>
          </div>
          <div class="part" id="status1">Status: None</div>
        </div>

        <!-- Second vertical section -->
        <div class="section">
          <div class="part">
            <form action="/blue_on" method="POST">
              <button id="button3">Button 3</button>
            </form>
          </div>
          <div class="part">
            <form action="/blue_off" method="POST">
              <button id="button4">Button 4</button>
            </form>
          </div>
          <div class="part" id="status2">Status: None</div>
        </div>
      </div>
    </main>

    <footer>
      <p>Microprocessor Project by MohammadJavad Shahbazi</p>
      <p>Master: Dr. Paiam Sanaee</p>
    </footer>
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
