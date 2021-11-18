from operationGPX import GPX
from navigation import nav
import time

stop = True
listeTrace=[1]
#file = '2021-11-08_556784540_Test.gpx'
trace = [10,5,10,15,10,25,10,35,20,35,30,35,30,45,30,55]
pos = [10,10,10,20,10,30,15,35,25,35,30,40,30,54]
orientation = 0
cpt=0
nav2 = nav()
gpx2 = GPX()
print(nav2.isFinish(trace,pos[12],pos[13]))

while stop:

    # Selection trace
    print("1 : Entrepot -> 2 Rue Papin")
    numTrace = input('Entrez le numero de la trace : ')
    if numTrace == 0:
        print("Arret du programme")
        stop = False
        time.sleep(1)
    elif numTrace in listeTrace:
        print("Vous avez choisi la trace ",numTrace)
        #trace=nav2.GpxToArray(file)
        if nav2.canStart(trace,9,4) == True:
            while (nav2.isFinish(trace,pos[cpt],pos[cpt+1]) == False):
                print(cpt)
                pointSuivant = nav2.nextPoint(trace,pos[cpt],pos[cpt+1])
                print(pointSuivant)
                nav2i = nav2.direction(pointSuivant,pos[cpt],pos[cpt+1],orientation)
                print(nav2i)
                if nav2i == "a droite":
                    orientation = 0
                if nav2i == "a gauche":
                    orientation = 90
                print(orientation)
                cpt += 2
            print("Vous etes arrive")
            time.sleep(1)
            continuer = input('Voulez-vous continuer: ')
            if continuer == 0:
                print("Arret du programme")
                stop = False
                time.sleep(1)
        else:
            print("Rentrez un autre numero")
            time.sleep(1)
    else:
        print("Rentrez un numero valide")
        time.sleep(1)



    
    

