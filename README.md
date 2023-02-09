# UMQTT
## Getting Started
These instructions will help you connect your Raspberry Pi Pico W to the internet and control the three LEDs on the add-on board using MQTT.

### Prerequisites
* Raspberry Pi Pico W
* OLED Display
* Three LEDs on the add-on board
* A MQTT server app
### Connecting to WiFi
1. Follow the Pico documentation to write the code for connecting to WiFi. [documentation for connecting to a wireless network](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf)
2. Once connected, print out the IP address of the Pico to the Shell.
### Installing umqtt simple module
Use the following command to install the umqtt simple module:
1. Click to 'Tool'choose 'Manage packages'
2. Type 'umqtt.simple'.
3. Choose 'micropython-umqtt.simple'
4. Click 'Install'
5. Add 'from umqtt.simple import MQTTClient' to your file
### Sending MQTT Messages
1. Create a JSON object to send as a message to your MQTT server app.
2. When you press a button on the Pico, the message will be sent to a topic of your choice.
### Controlling the LEDs
1. Create a scheme to control the brightness of the three LEDs on the add-on board.
2. Send a message to the Pico from your MQTT server app. The topic should be formatted as <something unique>/LED and the message should be in JSON format. For example, D1;50%.
3. The Pico should be subscribed to the same topic and receive the message.
4. The brightness of the LED called D1 should be adjusted to the required brightness using PWMs of a sufficiently high frequency.
5. Note: The full brightness will be 100% and off is 0%. The percentage should be converted into a PWM value.
### Displaying LED Information on OLED
The OLED should display the LED name and brightness level below the IP address from earlier.

## Conclusion
By following these steps, you should now be able to connect your Raspberry Pi Pico W to the internet and control the three LEDs on the add-on board using MQTT.
