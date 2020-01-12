from pushbullet.pushbullet import PushBullet
import json, os

def sendNotif () :
	pb = PushBullet("o.sqTG7BlAEOoQDpccJ2n3nFwZ4BRy2637")

	devices = pb.getDevices()
    
	title = "Recolteur d'eau"
	text = "Le reservoir est vide!"
    
	for device in devices:
		if device['pushable']:
        		note = pb.pushNote(device["iden"], title, text)
