# RaspberryPi Pico W Projects
![Lang](https://img.shields.io/badge/Language-MicroPython-lightblue)

- Thanks to [Dr. Payam Sanaee](https://example.com) for mentorship.

 



## Table of Contents
- [Web Server](#web-server)
- [Chip Temperature](#chip-temperature)
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

| Pico W Pin | LED Color  | Resistor |
|------------|------------|----------|
| GP15       | Red LED    | 220Ω     |
| GP16       | Blue LED   | 220Ω     |
| "LED"      | On-chip LED| -        |
| GND        | GND        | -        |

### Source requirment
- [Web Server](https://github.com/MoJavadSh/RaspberryPiPicoW/blob/main/WebServer.py)


## Chip Temperature
Using [Thingspeak](Thingspeak.com)
### Features
- Reads temperature data from the Pico W's onboard sensor.
- Sends data to ThingSpeak using HTTP POST requests.
- Uses two LEDs to indicate Wi-Fi connection status and data upload status.
- Uploads data when a button is pressed, with configurable fields on ThingSpeak.

### Hardware Requirements
- **Raspberry Pi Pico W**
- **Red LED** (connected to GPIO 16)
- **Blue LED** (connected to GPIO 20)
- **Push Button** (connected to GPIO 18 with a pull-up resistor)
- **Breadboard and jumper wires**

### Wiring Diagram

| Pico W Pin | Component     |
|------------|---------------|
| GP16       | Red LED       |
| GP20       | Blue LED      |
| GP18       | Push Button   |
| LED        | On-chip LED   |

### 🚀 How to Use

#### 1. Register on [Thingspeak](Thingspeak.com)
- create a new channel
- name the channel and make a field
- in API KEYS Header
   - copy Write API Key
   - paste in API part in code


### Source requirment
- [TempChart](https://github.com/MoJavadSh/RaspberryPiPicoW/blob/main/TempChart)





