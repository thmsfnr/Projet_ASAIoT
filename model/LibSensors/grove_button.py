#!/usr/bin/env python
#
# GrovePi Example for using the Grove Button (http://www.seeedstudio.com/wiki/Grove_-_Button)

import time
import grovepi

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3
def Button():
    grovepi.pinMode(button,"INPUT")
    while True:
        try:
            print(grovepi.digitalRead(button))
            time.sleep(.25)

        except IOError:
            print ("Error")


def Choix_trace():
    cpt = 0
    quitter = False
    res = 0
    while quitter == False:

        click = grovepi.digitalRead(button)
        if click == 1 :
            cpt += 1
        if click == 0 :
            if cpt >= 2 :
                res += 1
                cpt = 0
            elif cpt == 1 :
                quitter = True
            else :
                cpt = 0
        time.sleep(.25)
    return res