 # Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

WIDTH = 128 # oled display width
HEIGHT = 64 # oled display height

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=200000)  

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Init oled display
LedData = ["D1;50%", "D2;50%", "D3;50%", "D4;50%"] # create list to store Leds and Led's values
IP = "IP:"
def updateIP(IpAddress):
    global IP
    if(len(IpAddress) == 0):
        IP = "IP:"
    else:
        IP = "IP:" + IpAddress
        
def updateLedInfo(info):
    Led = info[0:2]
    global LedData
    for item in range(0, len(LedData)):
        if Led in LedData[item]:
            LedData[item] = info
            
def displayOled():
    # Clear the oled display in case it has junk on it.
    oled.fill(0)

     # Add some text (X,Y)
    oled.text(IP,0,5)
    oled.text(LedData[0],0,15)
    oled.text(LedData[1],50,15)
    oled.text(LedData[2],0,25)
    oled.text(LedData[3],50,25)

    # Finally update the oled display so the image & text is displayed
    oled.show()
