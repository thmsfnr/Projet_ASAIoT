from controller.navigation import nav
from view.interactionUser import User
from controller.useSensors import *
import time

"""Initialisation of the objects"""
nav2 = nav()
use = User()

"""Initialisation of main parameters"""
stop = True
allTrace=[[10,0,20,0,30,0,40,0]]
listeTrace = [1]

"""Course of the program"""
while stop:
    numTrace = use.chooseTrace()
    if numTrace == 0: # The user wants to quit the program
        afficheSurEcran("Arret du programme")
        time.sleep(2)
        stop = False
    elif numTrace in listeTrace: # The user has entered a valid num of trace
        afficheSurEcran("Vous avez choisi la trace "+str(numTrace))
        time.sleep(2)
        trace = allTrace[numTrace-1] # Obtaining the trace in table form
        nav2.navigationWithoutGps(trace) # A faire
        afficheSurEcran("La trace est terminee")
        time.sleep(2)
        stop = False
    else: # The user has entered an invalid num of trace
        afficheSurEcran("Rentrez un numero valide")
        time.sleep(2)
    