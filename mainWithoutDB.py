from operationGPX import GPX
from navigation import nav
from interactionUser import User
import time

stop = True
listeTrace=[1]
file = ["2021-11-08_556784540_Test.gpx"]

nav2 = nav()
gpx2 = GPX()
use = User()

while stop:

    numTrace = use.chooseTrace()
    if numTrace == 0:
        print("Arret du programme")
        stop = False
    elif numTrace in listeTrace:
        print("Vous avez choisi la trace ",numTrace)
        trace = gpx2.GpxToArray(file[numTrace-1])
        if nav2.canStart(trace,9,4) == True:
            nav2.navigation(trace)
            continuer = input('Voulez-vous continuer: ')
            if continuer == 0:
                print("Arret du programme")
                stop = False
        else:
            print("Rentrez un autre numero")
    else:
        print("Rentrez un numero valide")
