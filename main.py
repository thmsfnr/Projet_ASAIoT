import lectureGpx as nav

# Sélection trace
print("1 : Entrepot -> 2 Rue Papin")
numTrace = input('Entrez le numéro de la trace : ')
print("Vous avez choisi la trace ",numTrace)

# Récupérer trace
file = '2021-11-08_556784540_Test.gpx'
trace=nav.GpxToArray(file)

# Navigation
lat = 45.631000
lon = 4.097300
orientation = 320
pointSuivant = nav.encadrement(trace,lat,lon)
nav.direction(pointSuivant,lat,lon,orientation)

