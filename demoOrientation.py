
from view.interactionUser import User
from controller.useSensors import *
import time

"""Initialisation of the objects"""
use = User()

"""Initialisation of main parameters"""
stop = True

"""Course of the program"""
while stop:
    numTrace = use.chooseTrace()
    if numTrace == 0: # The user wants to quit the program
        afficheSurEcran("Arret du programme")
        time.sleep(2)
        stop = False
    elif numTrace == 1: # The user has entered a valid num of trace
        afficheSurEcran("Vous avez choisi la trace "+str(numTrace))
        time.sleep(2)
        afficheSurEcran("Debut du guidage")
        time.sleep(2)
        #vibrer(2)
        #vibrer(4)
        #vibrer(5)
        #vibrer(6)
        cpt = 0
        while cpt < 10:
            if (orientation()>45) and (orientation()<135):
                vibrer(2)
            elif ((orientation() >=0) and (orientation() <=45)) or ((orientation() >315) and (orientation() <360)):
                vibrer(5)
            elif (orientation() >=135) and (orientation() <225):
                vibrer(6)
            elif (orientation() >=225) and (orientation() <=315):
                vibrer(4)
            time.sleep(4)
            cpt += 1
        #vibrer(2)
        #vibrer(4)
        #vibrer(5)
        #vibrer(6)
        afficheSurEcran("La trace est terminee")
        time.sleep(2)
        stop = False
    else: # The user has entered an invalid num of trace
        afficheSurEcran("Rentrez un numero valide")
        time.sleep(2)
    