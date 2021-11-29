
import time
import grovepi

# Connect the Grove Vibration Motor to digital port D8
# SIG,NC,VCC,GND


def Vibrer(port):
    vibration_motor = port
    grovepi.pinMode(vibration_motor,"OUTPUT")
    try:
        # Start vibrating for 1 second
        grovepi.digitalWrite(vibration_motor,1)
        print ('start')
        time.sleep(.75)

        # Stop vibrating for 1 second, then repeat
        grovepi.digitalWrite(vibration_motor,0)
        print ('stop')
        time.sleep(1)
    except IOError:
        print ("Error")
