import driver_moisture
import driver_relay
import time
import grovepi

sensor = 1
while True : 
	H = grovepi.analogRead(sensor)
	print (H)
	if H  > 500 :
		driver_relay.OnOff(False)
	else :
		driver_relay.OnOff(True)
	print(driver_relay.testOnOff())
	time.sleep(2)
