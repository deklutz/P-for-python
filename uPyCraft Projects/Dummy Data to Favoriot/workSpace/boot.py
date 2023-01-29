import network
import utime as time

ssid="HANSOLO 5029" 
password="55712:Lr"


def rand( floor, mod=0, negative = False):
	# return random value from -floor.mod to floor.nod if negative is True
	from os import urandom as rnd

	sign = 1 if ord(rnd(1))%10 > 5 else -1
	sign = sign if negative else 1

	if mod:
		value = float(('{}.{}').format(ord(rnd(1))%floor, ord(rnd(1))%mod))
	else:
		value = int(('{}').format(ord(rnd(1))%floor))

	return sign*value

def connectToWifi(ssid, password):
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    print("Connecting to",ssid," wifi network....")  
    time.sleep(0.5)
  print('Connection successful')
  print(station.ifconfig())

connectToWifi(ssid, password)

