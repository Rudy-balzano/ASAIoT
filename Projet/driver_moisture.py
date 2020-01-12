import time
import grovepi

#Connectez le capteur d'humidite sur le port A1

sensor = 0

def humidity () :
	return grovepi.analogRead(sensor)  


