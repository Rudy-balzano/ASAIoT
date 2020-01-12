import driver_moisture
import driver_relay
import driver_weightSensor
import sendNotifPushBullet
import time
import grovepi

while True:
	H = driver_moisture.humidity()
	P = driver_weightSensor.peutLancer()
	if H < 300 and P :
		driver_relay.OnOff(True)
		time.sleep (100)
		driver_relay.OnOff(False)
		time.sleep(1000)
	elif !P : 
		sendNotifPushBullet.sendNotif()
		i = 0
		while !P and i < 500 : 
			i = i+1
			time.sleep(2)

