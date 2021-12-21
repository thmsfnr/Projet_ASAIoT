
import serial, time

ser = serial.Serial('/dev/ttyACM0',  9600, timeout = 0)	#Open the serial port at 9600 baud
ser.flush()

class GPS:
	#The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
	inp=[]
	# Refer to SIM28 NMEA spec file http://www.seeedstudio.com/wiki/images/a/a0/SIM28_DATA_File.zip
	GGA=[]


	#Read data from the GPS
	def read(self):	
		while True:
			GPS.inp=ser.readline()
			if (str(GPS.inp[:6]))[2:8] =='$GPRMC': # GGA data , packet 1, has all the data we need
				break
			time.sleep(0.1)     #without the cmd program will crash
		GPS.GGA=str(GPS.inp).split(",")	#Split the stream into individual parts
		return [GPS.GGA]
		
	#Split the data into individual elements
	def vals(self):
		
		lat=GPS.GGA[3]
		lat_ns=GPS.GGA[4]
		lon=GPS.GGA[5]
		lon_ew=GPS.GGA[6]
		
		return [lat,lat_ns,lon,lon_ew]
	
	# Convert to decimal degrees
	def decimal_degrees(self, raw_degrees):
		try:
			degrees = float(raw_degrees) // 100
			d = float(raw_degrees) % 100 / 60
			return degrees + d
		except: 
			return raw_degrees



def get_position():
	
	g=GPS()

	x=g.read()
	while x == []:
		x=g.read()	#Read from GPS

	[lat,lat_ns,lon,lon_ew]=g.vals()	#Get the individial values
	
	lat = g.decimal_degrees(float(lat))
	if lat_ns == "S": 
		lat = -lat
	
	lon = g.decimal_degrees(float(lon))
	if lon_ew == "W":
		lon = -lon

	return [lat,lon]

				
