from model.operationGPX import GPX
from controller.navigation import nav
from view.interactionUser import User
from model.interactionDB import DB

"""Initialisation of the objects"""
nav2 = nav()
gpx2 = GPX()
use = User()
db = DB()

gpx2.GPXToDB("/home/pi/Projet_ASAIoT/Examples_GPX/2021-11-08_556784540_Test.gpx","1 : Entrepot -> 2 Rue Papin")

"""Initialisation of main parameters"""
stop = True
listeTrace=db.selectAllIdTrace()

"""Course of the program"""
while stop:

    numTrace = use.chooseTrace()
    if numTrace == 0: # The user wants to quit the program
        print("Arret du programme")
        stop = False
    elif numTrace in listeTrace: # The user has entered a valid num of trace
        print("Vous avez choisi la trace ",numTrace)
        trace = gpx2.dataGpxToArray(numTrace) # Obtaining the trace in table form
        if nav2.canStart(trace,9,4) == True: # The user can start the trace
            nav2.navigation(trace) # Calculation and display of the direction to follow
            continuer = input('Voulez-vous continuer: ')
            if continuer == 0: # The user wants to quit the program
                print("Arret du programme")
                stop = False
        else: # The user wants to continue the program
            print("Rentrez un autre numero")
    else: # The user has entered an invalid num of trace
        print("Rentrez un numero valide")
    

