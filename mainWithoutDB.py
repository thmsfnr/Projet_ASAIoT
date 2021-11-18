from operationGPX import GPX
from navigation import nav
from interactionUser import User
import time

stop = True
listeTrace=[1]
trace = [10,5,10,15,10,25,10,35,20,35,30,35,30,45,30,55]
pos = [10,10,10,20,10,30,15,35,25,35,30,40,30,52,30,54]
orientation=[0,0,0,0,90,90,0]
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
        if nav2.canStart(trace,9,4) == True:
            nav2.navigation(trace,pos,orientation)
            continuer = input('Voulez-vous continuer: ')
            if continuer == 0:
                print("Arret du programme")
                stop = False
        else:
            print("Rentrez un autre numero")
    else:
        print("Rentrez un numero valide")
