import time
import grovepi

# Connect the Grove Relay to digital port D2
# SIG,NC,VCC,GND

relay = 2


def OnOff (value) :  #permet d'allumer le relay. Prends en parametre True ou False.
	if value :
		grovepi.digitalWrite(relay,1)  #Si on entre true, met le relay en marche
		print(testOnOff())
	else :
		grovepi.digitalWrite(relay,0)  #Sinon, etteint le relay
		print("off")


def testOnOff ():
	r = grovepi.digitalRead(relay)
	if r == 1:
		return "On"
	else : 
		return "Off"

