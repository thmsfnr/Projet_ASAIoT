
import math
import sys  
from pathlib import Path  
file = Path("operationGPX.py").resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))  

import xml.etree.ElementTree as ET
from model.interactionDB import DB

db = DB()

class GPX:
    
    def init():
        """Initialisation of gpx"""

        print("OK")

    def GpxToArray(self,file):
        """Read a gpx file and put its content in an array"""

        trace=[]
        tree = ET.parse(file)
        root = tree.getroot()
        for i in root[1][1]:
            trace.append(i.attrib['lat'])
            trace.append(i.attrib['lon'])
        return trace # Array

    def GPXToDB(self,file,nomTrace):
        """Read a gpx file and put its content in a database"""

        db.insertTrace(nomTrace)
        tree = ET.parse(file)
        root = tree.getroot()
        for i in root[1][1]:
           db.insertTrace(db.selectTraceWithName(nomTrace),i.attrib['lat'],i.attrib['lon'])

    def dataGpxToArray(self,idTrace):
        """Read a trace in a database and put its content in an array"""
        
        trace=[]
        requete = db.selectDataWithIdTrace(idTrace)
        for i in requete:
            trace.append(requete[i][0])
            trace.append(requete[i][1])
        return trace # Array

    def convertDegreeToMeter(self,tab):
        """Convert a tab of latitude and longitude in degree into meter"""

        for i in range(0,len(tab)-1,2):
            tab[i] = tab[i] * 111,32
            tab[i+1] = 40075 * (math.cos(tab[i])/360)
        return tab

    def convertMeterToTime(self,speed,tab):
        """Convert a tab of latitude and longitude in meter into time"""

        for i in range(0,len(tab)):
            t = d/v
            tab[i]=