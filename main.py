import time
from umqtt.simple import MQTTClient
from MqttConnection import listenBroker
from WifiConnection import connectWifi
def main():
    
    listenBroker()
    #print(connectWifi())

if __name__ == "__main__":
    main()