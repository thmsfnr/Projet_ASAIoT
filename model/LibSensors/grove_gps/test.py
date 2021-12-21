# Import de la librairie serial
import serial

# Ouverture du port serie avec :
# '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
# 9600 : vitesse de communication
serialArduino = serial.Serial('/dev/ttyACM0', 9600)

def cleanstr(in_str):
	out_str = "".join([c for c in in_str if c in "0123456789.-" ])
	if len(out_str)==0:
		out_str = "-1"
	return out_str

def safefloat(in_str):
	try:
		out_str = float(in_str)
	except ValueError:
		out_str = -1.0
	return out_str

# Ecriture de chaque message recu
while True :
  	print(serialArduino.readline())