#!/usr/bin/env python
import time
import bme680
import os
from time import sleep
from datetime import datetime


try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

file=open("/home/pi/data_log.csv","a")

if os.stat("/home/pi/data_log.csv").st_size == 0:
     file.write("Time,Temperature,Pressure,Humidity\n")


               
                  
                  


try:
    while True:
        
        now=datetime.now()
        if sensor.get_sensor_data():
             
             
             
          
	  
	    file.write(str(now)+","+str(sensor.data.temperature)+","+str(sensor.data.pressure)+","+str(sensor.data.humidity)+"\n")
            file.flush()
	    time.sleep(120)	
                        
	       
                  
                  

except KeyboardInterrupt:
    pass
