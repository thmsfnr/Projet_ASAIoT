
'''
try:
	acc_mag=lsm303d.lsm303d()

	while True:
		
		# Get accelerometer values
		acc=acc_mag.getRealAccel()
		
		# Wait for compass to get ready
		while True:
			if acc_mag.isMagReady():
				break
				
		# Read the heading
		heading= acc_mag.getHeading()
		
		print("Acceleration of X,Y,Z is %.3fg, %.3fg, %.3fg" %(acc[0],acc[1],acc[2]))
		print("Heading %.3f degrees\n" %(heading))

except IOError:
	print("Unable to read from accelerometer, check the sensor and try again")
'''

def getOrientation():
	try:
		acc_mag=lsm303d.lsm303d()

		while True:
			
			# Get accelerometer values
			acc=acc_mag.getRealAccel()
			
			# Wait for compass to get ready
			while True:
				if acc_mag.isMagReady():
					break
					
			# Read the heading
			heading= acc_mag.getHeading()
			
			#print("Acceleration of X,Y,Z is %.3fg, %.3fg, %.3fg" %(acc[0],acc[1],acc[2]))
			print("Heading %.3f degrees\n" %(heading))

	except IOError:
		print("Unable to read from accelerometer, check the sensor and try again")
	return heading
