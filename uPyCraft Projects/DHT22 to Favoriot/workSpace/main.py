from machine import Pin
from time import sleep
import dht
import network

#to define dht object called DHT22_Sensor on specified pin
DHT11_Sensor=dht.DHT11(Pin(14))

url='https://apiv2.favoriot.com/v2/streams'
Device_Developer_ID='DHT11sensor@hanindr' #adjust 
Access_Token='QZy2lTui5gXuwiR6A8PUazbfsQS8aW01' #adjust

while True:
  #add this try & except loop to avoid ESP32 from crashing
  #when cannot read data from the sensor
  try:
    sleep(8) #max sampling rate is 2sec
    
    #need to call this before requesting T & H readings
    DHT11_Sensor.measure()
    T = DHT11_Sensor.temperature()
    H = DHT11_Sensor.humidity()
    
    #Let's print the measure T & H of this room
    print ("The room temperature is", T, "oC")
    print ("The room humidity is", H, "%")
    print()
    print('----------------------------------')
    
    data_sensor={
    'device_developer_id':Device_Developer_ID,
    'data':{
      'field1':T,
      'field2':H,
      }
     }
     
  requests_header={
    'Content-Type': 'application/json',
    'Apikey':Access_Token
    }
    
  data_submission=urequests.post(url,json=data_sensor,headers=requests_header)
  
  print('Data submission status on  Favoriot is', data_submission.status_code)
  data_submission.close()
  print('********************************')
  time.sleep(8)
  
  except OSError as e:
    print('Failed to read data from sensor!')


