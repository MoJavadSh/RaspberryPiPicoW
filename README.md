# RaspberryPi Pico W Projects
![Lang](https://img.shields.io/badge/Language-MicroPython-lightblue)

- Thanks to [Dr. Payam Sanaee](https://example.com) for mentorship.
- Inspired by [Awesome IoT Projects](https://github.com/awesome-iot).
 



## Table of Contents
- [Web Server](#web-server)
- [Soon](#Soon)
- [Soon](#Soon)
- [Soon](#Soon)


## Web Server
### Features
- Control red and blue LEDs through a web browser.
- Onboard LED indicates the status of the Wi-Fi connection:
  - **Solid ON for 5 seconds**: Successfully connected.
  - **Rapid blinking**: Wi-Fi connection failed.
- Displays the Pico W's IP address in the Thonny IDE shell for easy access.
###  Hardware Requirements
- **Raspberry Pi Pico W**
- **Red LED**
- **Blue LED**
- **2 x 220Ω resistors**
- **Breadboard and jumper wires**
### Wiring Diagram

| Pico W Pin | LED Color | Resistor |
|------------|-----------|----------|
| GP15       | Red LED   | 220Ω     |
| GP16       | Blue LED  | 220Ω     |
| "LED"      | LED       | -        |
| GND        | GND       | -        |

### Source requirment
- [Web Server](https://github.com/MoJavadSh/RaspberryPiPicoW/blob/main/WebServer.py)



