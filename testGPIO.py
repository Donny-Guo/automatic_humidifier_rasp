import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)


def HumdOn():
    print("Turn On")
    GPIO.output(16,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(16,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(16,GPIO.HIGH)
    
def HumdOff():
    print("Turn OFF")
    GPIO.output(16,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(16,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(16,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(16,GPIO.HIGH)
    
    
    
    
    
    
print("Turn on")
GPIO.output(16,GPIO.HIGH)

time.sleep(0.1)

print("Turn OFF")
GPIO.output(16,GPIO.LOW)

time.sleep(0.1)

print("Turn On")
GPIO.output(16,GPIO.HIGH)


# OFF
time.sleep(5)




print("Turn OFF")
GPIO.output(16,GPIO.LOW)

time.sleep(0.1)

print("Turn On")
GPIO.output(16,GPIO.HIGH)
time.sleep(0.1)



print("Turn OFF")
GPIO.output(16,GPIO.LOW)

time.sleep(0.1)

print("Turn On")
GPIO.output(16,GPIO.HIGH)
