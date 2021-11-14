from operationGPX import GPX
from navigation import nav



"""
# Selection trace
print("1 : Entrepot -> 2 Rue Papin")
numTrace = input('Entrez le numero de la trace : ')
print("Vous avez choisi la trace ",numTrace)"""

"""
# Recuperer trace
file = '2021-11-08_556784540_Test.gpx'
trace=nav.GpxToArray(file)"""


"""
# Navigation
lat = 45.631000
lon = 4.097300
orientation = 320
pointSuivant = nav.encadrement(trace,lat,lon)
nav.direction(pointSuivant,lat,lon,orientation)"""

#Test de navigation
trace = [10,5,10,15,10,25,10,35,20,35,30,35,30,45,30,55]
pos = [10,10,10,20,10,30,15,35,25,35,30,40,30,44,30,44]
orientation = 0
for i in range(0,len(trace),2):
    pointSuivant = nav.encadrement(trace,pos[i],pos[i+1])
    print(pointSuivant)
    navi = nav.direction(pointSuivant,pos[i],pos[i+1],orientation)
    print(navi)
    if navi == "a droite":
        orientation = 0
    if navi == "a gauche":
        orientation = 90
    print(orientation)

