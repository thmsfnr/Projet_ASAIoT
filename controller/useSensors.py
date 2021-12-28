
import sys  
from pathlib import Path  
file = Path("useSensors.py").resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))  

from model.LibSensors.driverI2C import *
from model.LibSensors.groveCompass import *
from model.LibSensors.grove_button import *
from model.LibSensors.groveVibration import *
from model.LibSensors.grove_gps.grove_gps_data import *
  
def afficheSurEcran(text):
    """Display the desired text on the lcd screen"""

    setText(text)

def changerCouleur(color):
    """Change the colour of the LCD screen"""

    setColor(color)

def orientation():
    """Return the orientation of the deliverer"""

    return getOrientation()

def vibrer(port):
    """Vibrate the vibrator that corresponds to the port"""

    Vibrer(port)

def ChoixTrace():
    """Operate the Button to select a track"""

    return Choix_trace()

def position():
    """Return the position of the deliverer"""

    return get_position()
