import serial


def poids () : 
	ser = serial.Serial('/dev/ttyACMO',9600)
	p = ser.readline()
	return p


def peutLancer () :
	p = poids 
	if p < 10 : ## 
		return False
	else : 
		return True
