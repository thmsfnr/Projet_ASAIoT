# coding: utf-8

from driverI2C import *
import time
import sys

#while True:
#echoing()
#setText("Salut Polytech! Test ecran LCD jfhgdhfgdhfgfhg")
#time.sleep(2)

#while True:
#	setColor("violet")
#	time.sleep(1)
#	setColor("vert")
#	time.sleep(1)
#	setColor("blanc")
#	time.sleep(1)

setText("Salut Polytech! Test ecran LCD")
setRGB(0,128,64)
time.sleep(2)

for c in range(0,200):
	setRGB(c,200-c,0)
	time.sleep(0.1)
setRGB(0,255,0)
setText("Bye!")
