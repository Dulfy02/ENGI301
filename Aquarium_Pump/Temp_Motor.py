#Adulfo Amador
#Rice University 
#ENGI 301 - Fall 2018

#This code will take the temperature DHT11 sensor
#and display them on a screen.
#See Hackster for a more detailed description of the project.


#imports
import os
import glob
import time
import Adafruit_BBIO.GPIO as GPIO
import time
import random
import os



# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

BUTTON0                      = "P1_29"
MOTOR0                       = "P1_36"

# ------------------------------------------------------------------------
# Main Tasks
# ------------------------------------------------------------------------

 # Initialize Button
GPIO.setup(BUTTON0, GPIO.IN)
GPIO.setup(MOTOR0, GPIO.OUT)
    
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f
        

def temp():
    image_choices = ['Screen_Display.jpg']
    command = 'sudo /var/lib/cloud9/ENGI301/Aquarium_Pump/display.sh ' + image_choices[0]
    print(command)
    os.system(command)
    time.sleep(5)

temp()

        
input = GPIO.input(BUTTON0)

while True:
    while (GPIO.input(BUTTON0) == 1):
        GPIO.output(MOTOR0, 1)
        print("Motor running")
        time.sleep(1)
        
        if (GPIO.input(BUTTON0) == 0):
            GPIO.output(MOTOR0, 0)
            print("Stopped")
            break
        
    print(read_temp())	
    time.sleep(300)
	
	

        

	
	
