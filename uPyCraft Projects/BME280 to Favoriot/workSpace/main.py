from machine import Pin, SoftI2C
from time import sleep
import BME280
import urequests

url='https://apiv2.favoriot.com/v2/streams'
Device_Developer_ID='BME280sensor@hanindr' #adjust 
Access_Token='VDrzk0JVQpzKrpaTHmC1zK4TFyV9ZEcu' #adjust

#i2c declaration
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

while True:
  #1. Obtain real data from BME280 sensor
  bme = BME280.BME280(i2c=i2c)
  t = bme.temperature[:-1]
  h = bme.humidity[:-1]
  p = bme.pressure[:-3]
  
  T = float(t)
  H = float(h)
  P = float(p)
  print ('The current temperature is', t)
  print ('The current humidity is', h)
  print ('The current pressure is', p)
  print()
  
  sleep (8)
  
  led = Pin(2, Pin.OUT)
  
  if T < 25.0:
    led.value (not led.value())
    sleep (0.05)
  else:
    led.value (not led.value())
    sleep (1)

  data_sensor={
    'device_developer_id':Device_Developer_ID,
    'data':{
      'field1':t,
      'field2':h,
      'field3':p
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
 
  



