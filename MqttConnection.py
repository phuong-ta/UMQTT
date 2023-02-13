import time
from machine import Pin, Timer
from umqtt.simple import MQTTClient
from WifiConnection import connectWifi
from JsonController import readJson
from OledController import displayOled

# Set up the button and light pins as inputs and outputs
button = Pin(8, Pin.IN, Pin.PULL_UP)
#
IP = connectWifi() # ip address
topic = b"Phuong/LED"
c = MQTTClient(b"phuong", b"broker.hivemq.com")
"""
c = MQTTClient(client_id=b"bigles",
    server=b"broker.hivemq.com", # home: bec3bbc6c9c44b4fae7e5a42781338c5.s2.eu.hivemq.cloud - school: 192.168.1.254
    port=8883, #home: 8883 - school: ''
    user=None, #home: tester - school: ''
    password=None, #home: 12345678 - school: ''
    keepalive=3600,
    ssl=True,
    ssl_params={'server_hostname':'broker.hivemq.com'} # home: bec3bbc6c9c44b4fae7e5a42781338c5.s2.eu.hivemq.cloud - school: ''
)
"""
c.connect()
# callback for received subscription messages
def sub_cb(topic, msg):
    print((topic, msg))
    # controll led here

# Publish a message.
def publishMsg():
    c.publish(topic, readJson())
    
def listenBroker():
    print(IP)
    c.set_callback(sub_cb)
    c.subscribe(topic)
    tim = Timer()
    while True:
        c.check_msg()  # Non-blocking wait for message
        displayOled()
        if not button.value():
            # Publish message if the button is pressed
            tim.init(mode=Timer.ONE_SHOT, period=100, callback=lambda t:publishMsg())     
    
