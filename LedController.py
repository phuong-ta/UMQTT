from machine import Pin, PWM

led_board = Pin("LED", Pin.OUT)
led_d1 = Pin(22, Pin.OUT)
led_d2 = Pin(21, Pin.OUT)
led_d3 = Pin(20, Pin.OUT)


def controllLed(LedName, Ledlevel):
    print (LedName + Ledlevel)
    LedID = 20
    if LedName =="D1":
        LedID = 22
    elif LedName =="D2":
        LedID = 21
    elif LedName =="D3":
        LedID = 20

    pwm_led = PWM(Pin(LedID, mode=Pin.OUT)) # Attach PWM object on the LED pin
    pwm_led.freq(1_000) # set freq 1000
    pwm_led.duty_u16(int((int(Ledlevel)/100)*65_535)) # control brightless with precent