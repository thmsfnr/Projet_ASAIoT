
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
            trace.append(float(i.attrib['lat']))
            trace.append(float(i.attrib['lon']))
        return trace # Array

    def GPXToDB(self,file,nomTrace):
        """Read a gpx file and put its content in a database"""

        db.insertTrace(nomTrace)
        tree = ET.parse(file)
        root = tree.getroot()
        for i in root[1][1]:
           db.insertTrace(db.selectTraceWithName(nomTrace))

    def dataGpxToArray(self,idTrace):
        """Read a trace in a database and put its content in an array"""
        
        trace=[]
        requete = db.selectDataWithIdTrace(idTrace)
        for i in requete:
            trace.append(requete[i][0])
            trace.append(requete[i][1])
        return trace # Array

    def convertDegreeToMeter(self,trace):
        """Convert a tab of latitude and longitude in degree into meter"""

        res = [0]
        for i in range(0,len(trace)-1,2):
            distLat = abs((trace[i]* 111,32)-(trace[i+2]* 111,32))
            distLon = abs((40075 * (math.cos(trace[i])/360))-(40075 * (math.cos(trace[i+2])/360)))
            dist = math.sqrt(distLat**2)+math.sqrt(distLon**2)
            res.append(dist)
        return res

  