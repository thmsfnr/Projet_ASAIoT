from model.operationGPX import GPX
from controller.navigation import nav
from view.interactionUser import User
from controller.useSensors import *

"""Initialisation of main parameters"""
stop = True
listeTrace=[1]
file = ["/home/pi/Projet_ASAIoT/Examples_GPX/test2.gpx"]
 
"""Initialisation of the objects"""
nav2 = nav()
gpx2 = GPX()
use = User()

"""Course of the program"""
while stop:

    numTrace = use.chooseTrace()
    if numTrace == 0: # The user wants to quit the program
        afficheSurEcran("Arret du programme")
        stop = False
    elif numTrace in listeTrace: # The user has entered a valid num of trace
        afficheSurEcran("Vous avez choisi la trace "+str(numTrace))
        trace = gpx2.GpxToArray(file[numTrace-1]) # Obtaining the trace in table form
        startPos = get_position()
        if nav2.canStart(trace,startPos[0],startPos[1]) == True: # The user can start the trace
            nav2.navigation(trace) # Calculation and display of the direction to follow
            afficheSurEcran("La trace est terminee")
            stop = False
        else: # The user wants to continue the program
            afficheSurEcran("Trace non demarrable")
    else: # The user has entered an invalid num of trace
        afficheSurEcran("Rentrez un numero valide")
