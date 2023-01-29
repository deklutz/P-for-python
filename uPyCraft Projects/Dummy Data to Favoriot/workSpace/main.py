from time import sleep
import urequests
import random

url='https://apiv2.favoriot.com/v2/streams'
Device_Developer_ID='dummysensor@hanindr'
Access_Token='xfeXn8Qhf1OLx3dABWvZ9YOiV31AnUL3'

while True:
  #1. Generate random data for three dummy sensors
  t = float(random.randrange(15, 40)) #unit in Celsius
  h = float(random.randrange(60, 90)) #usually in percent
  p = float(random.randrange(900, 1500)) #unit in hPa
  
  print ('The current temperature is', t, 'oC')
  print ('The current humidity is', h, '%')
  print ('The current pressure is', p, 'hPa')
  print()
  
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
  time.sleep(15)
 


