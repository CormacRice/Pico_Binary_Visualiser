from machine import Pin

from time import sleep

ledPin1 = Pin(15, Pin.OUT)
ledPin2 = Pin(14, Pin.OUT)
ledPin3 = Pin(13, Pin.OUT)
ledPin4 = Pin(12, Pin.OUT)

while True:
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(1)
    sleep(.5)
    
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(1)
    sleep(.5)
    
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(1)
    sleep(.5)
    
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(1)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(1)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(1)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(1)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(0)
    sleep(.5)
    
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(1)
    sleep(.5)