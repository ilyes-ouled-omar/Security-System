import RPi.GPIO as gpio
import time
import spidev
import os

GPIO.setwarnings(False)
GPIO.setmode(gpio.BOARD)

pir1=11
pir2=7
buzzer=13
green_led=15
red_led=17

GPIO.setup(pir1, gpio.IN)         #Read output from PIR1 sensor
GPIO.setup(pir2, gpio.IN)         #Read output from PIR2 sensor

GPIO.setup(13, gpio.OUT)    #buzzer output pin
GPIO.setup(15, gpio.OUT)     # green led   
GPIO.setup(17, gpio.OUT)     #red led      

#Open SPI bus

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
 
def ConvertTemp(data,places):
 
  # ADC Value
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 330)/float(1023))-50
  temp = round(temp,places)
  return temp
 
# Define sensor channels
light_channel = 0
temp_channel  = 1
 
# Define delay between readings
delay = 5
 







#===================




while True :
     
  # Read the light sensor data
       light_level = ReadChannel(light_channel)
       light_volts = ConvertVolts(light_level,2)
 
  # Read the temperature sensor data
        temp_level = ReadChannel(temp_channel)
        temp_volts = ConvertVolts(temp_level,2)
        temp       = ConvertTemp(temp_level,2)
        pir1_input=GPIO.input(pir1)
        pir2_input=GPIO.input(pir2)
        if pir1_input==0 and pir2_input==0 :
            gpio.output(buzzer,False)
            gpio.output(green_led,False)
            gpio.output(red_led,False)
        if pir1_input==1 and pir2_input==0 :
            gpio.output(buzzer,True)
            gpio.output(red_led,True)
            print("detecting animal ")
        if pir1_input==1 and pir2_input==1 :
            gpio.output(buzzer,True)
            gpio.output(green_led,True)
            print("detecting human")
        if temp>35 :
            print ("detecting fire in temperature={} ".format(temp))
            gpio.output(buzzer,True)
        if light_level>600:
            gpio.output(buzzer,True)

            
            
