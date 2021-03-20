import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

pir1=11
pir2=7
buzzer=13
green_led=15
red_led=17

gpio.setup(pir1, gpio.IN)         #Read output from PIR1 sensor
gpio.setup(pir2, gpio.IN)         #Read output from PIR2 sensor

gpio.setup(13, gpio.OUT)    #buzzer output pin
gpio.setup(15, gpio.OUT)     # green led   
gpio.setup(17, gpio.OUT)     #red led      

gpio.setup(36, gpio.IN)    #buzzer output pin
gpio.setup(38, gpio.IN)     # green led   
gpio.setup(40, gpio.IN)     #red led      

while  True :
        pir1_input=gpio.input(pir1)
        pir2_input=gpio.input(pir2)
        
        pin1=gpio.input(36)
        pin2=gpio.input(38)
        pin3=gpio.input(40)

        
            
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
        if  (pin1==1 and pin2==0 and pin3==0)   :
            print ("detecting high temperature")
            gpio.output(buzzer,True)

        if  (pin1==0 and pin2==0 and pin3==1)  :
            gpio.output(buzzer,True)
            print("detecting gaz")
        if (pin1==0 and pin2==1 and pin3==0):
            gpio.output(buzzer,True)
            print ("detecting light")
        if (pin1==1 and pin2==1 and pin3==0):
            print ("detecting high temperature and high light")
            gpio.output(buzzer,True)
         if (pin1==1 and pin2==0 and pin3==1):
            print ("detecting high temperature and high percent of gaz")
            gpio.output(buzzer,True)
         if (pin1==0 and pin2==1 and pin3==1):
            print ("detecting high light and high percent of gaz")
            gpio.output(buzzer,True)
         if (pin1==1 and pin2==1 and pin3==1):
            print ("detecting high temperature and high percent of gaz and high light")
            gpio.output(buzzer,True)
         if (pin1==0 and pin2==0 and pin3==0):
             gpio.output(buzzer,False)
             print("evry thing is ok")
         time.sleep(0.1)
