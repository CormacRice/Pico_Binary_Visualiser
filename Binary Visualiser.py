from machine import Pin

ledPin1 = Pin(15, Pin.OUT)
ledPin2 = Pin(14, Pin.OUT)
ledPin3 = Pin(13, Pin.OUT)
ledPin4 = Pin(12, Pin.OUT)

binary = input("What number would you like in Binary?")
print(binary)

if (binary == "0"):
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(0)
    
elif (binary == "1"):
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(1)
    
elif (binary == "2"):
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(0)
    
elif (binary == "3"):
    ledPin1.value(0)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(1)
    
if (binary == "4"):
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(0)
    
elif (binary == "5"):
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(1)
    
elif (binary == "6"):
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(0)
    
elif (binary == "7"):
    ledPin1.value(0)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(1)
        
if (binary == "8"):
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(0)
    
elif (binary == "9"):
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(0)
    ledPin4.value(1)
    
elif (binary == "10"):
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(0)
    
if (binary == "11"):
    ledPin1.value(1)
    ledPin2.value(0)
    ledPin3.value(1)
    ledPin4.value(1)
    
elif (binary == "12"):
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(0)
    
elif (binary == "13"):
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(0)
    ledPin4.value(1)
    
elif (binary == "14"):
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(0)
    
elif (binary == "15"):
    ledPin1.value(1)
    ledPin2.value(1)
    ledPin3.value(1)
    ledPin4.value(1)
    
