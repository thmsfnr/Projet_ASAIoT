
import sys  
from pathlib import Path  
file = Path("interactionUser.py").resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))  

from controller.useSensors import * 
from model.interactionDB import DB

db = DB()

class User:
    
    def init():
        """Initialisation of the user"""

        print("OK")

    def chooseTraceTerminal(self):
        """Ask to the user to choose a trace"""

        print("1 : Entrepot -> 2 Rue Papin")
        print("2 : Entrepot -> 2 Rue Polytech")
        print("3 : Entrepot -> 2 Rue Apple")
        numTrace = input('Entrez le numero de la trace : ')
        return numTrace # String

    def chooseTrace(self):
        """Ask to the user to choose a trace"""

        afficheSurEcran("1 : Entrepot -> 2 Rue Papin")
        numTrace = ChoixTrace()
        return numTrace

    def chooseTraceDB(self):
        """Ask to the user to choose a trace"""

        cpt = 1
        for i in db.selectAllNameTrace:
            afficheSurEcran(str(cpt) + str(i))
            cpt+=1
        numTrace = ChoixTrace()
        return numTrace
    

