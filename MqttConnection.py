from machine import Pin, Timer
from umqtt.simple import MQTTClient
from WifiConnection import connectWifi
from JsonController import readJson
from OledController import displayOled, updateIP, updateLedInfo
from LedController import controllLed

# Set up the button as inputs
button = Pin(8, Pin.IN, Pin.PULL_UP)
#
IP = connectWifi() # ip address
updateIP(IP)
topic = b"Phuong/LED"
#c = MQTTClient(b"phuong", b"broker.hivemq.com") # local boker

# cloud
c = MQTTClient(client_id=b"bigles",
    server=b"<your cloud>", 
    port=8883, 
    user=b"<your user name>", 
    password=b"<your password>", 
    keepalive=3600,
    ssl=True,
    ssl_params={'server_hostname':'<your cloud>'} 
)

c.connect()
# callback for received subscription messages
def sub_cb(topic, msg):
    #print((topic, msg))
    newData = msg.decode() # convert binary to string
    updateLedInfo(newData) # update LED info
    # get led name and level for controll level of led
    LedName = newData[0:2]
    LedLevel = newData[3:-1]
    controllLed(LedName, LedLevel)

# Publish a message.
def publishMsg():
    c.publish(topic, readJson())
    
def listenBroker():
    c.set_callback(sub_cb)
    c.subscribe(topic)
    tim = Timer()
    while True:
        c.check_msg()  # Non-blocking wait for message
        displayOled()
        if not button.value():
            # Publish message if the button is pressed
            tim.init(mode=Timer.ONE_SHOT, period=100, callback=lambda t:publishMsg())    
    
