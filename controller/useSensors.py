
import sys  
from pathlib import Path  
file = Path("useSensor.py").resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))  

from model.LibSensors.driverI2C import *
from model.LibSensors.groveCompass import *
from model.LibSensors.grove_button import *
from model.LibSensors.groveVibration import *

'''
import time
import sys
'''

#       La fonction affiche sur l'ecran lcd le texte qu'on souhaite     
def afficheSurEcran(texte):
    setText(texte)

#       La fonction Change la couleur de l'ecran LCD
def changerCouleur(couleur):
    setColor(couleur)

#       La fonction renvoie l'orientation du livreur    
def orientation():
    return getOrientation()


"""
#       TEST    
#orientation()
afficheSurEcran("ayoub")
changerCouleur("blanc")
#print(Choix_trace())

print(Vibrer(2))"""