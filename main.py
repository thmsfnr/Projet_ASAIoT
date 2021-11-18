from operationGPX import GPX
from navigation import nav
from interactionUser import User
from interactionDB import DB
import time

nav2 = nav()
gpx2 = GPX()
use = User()
db = DB()

stop = True
listeTrace=db.selectAllIdTrace()

while stop:

    numTrace = use.chooseTrace()
    if numTrace == 0:
        print("Arret du programme")
        stop = False
    elif numTrace in listeTrace:
        print("Vous avez choisi la trace ",numTrace)
        trace = gpx2.dataGpxToArray(numTrace)
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
    

