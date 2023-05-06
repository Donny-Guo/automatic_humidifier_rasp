import time
import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Humidifier function
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
    
# Humidifier setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)


# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
text = "humidity = " + str(50) + " %"
humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
HumdOn()
IsOn = True
text1 = "humidity = 30%"
text2 = "temperature = 20C"
SensorError = False
while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    if humidity is not None and temperature is not None:
        text1 = "humidity = " + str(humidity) + " %"
        text2 = "temperature = " + str(temperature) + " C"
        SensorError = False
    else:
        SensorError=True
        temperature = 24
        if IsOn:
            humidity = 30
        else:
            humidity = 90
    if (IsOn):
        text3 = "Humidifier is on."
    else:
        text3 = "Humidifier is off."
    
    if (SensorError):
        text4 = "Sensor not working"
    else:
        text4 = "Sensor is working"
    # Write two lines of text.

    draw.text((x, top),  text1,  font=font, fill=255)
    draw.text((x, top+8),  text2, font=font, fill=255)
    draw.text((x, top+16),  text3, font=font, fill=255)
    draw.text((x, top+24),  text4, font=font, fill=255)	
    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)
    if humidity >= 80:
        if IsOn == True:
            HumdOff()
            IsOn = False
    else:
        if humidity < 78 and IsOn == False:
            HumdOn()
            IsOn = True
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
