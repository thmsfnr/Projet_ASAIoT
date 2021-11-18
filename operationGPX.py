import xml.etree.ElementTree as ET
from interactionDB import DB

db = DB()

class GPX:
    
    def init():
        print("OK")

    def GpxToArray(self,file):
        trace=[]
        tree = ET.parse(file)
        root = tree.getroot()
        #return("L'element racine : ", root.tag)
        #return("Le premier enfant de la racine : ", root[1][1].tag)
        for i in root[1][1]:
            trace.append(i.attrib['lat'])
            trace.append(i.attrib['lon'])
        return trace

    def GPXToDB(self,file,nomTrace):
        db.insertTrace(nomTrace)
        tree = ET.parse(file)
        root = tree.getroot()
        for i in root[1][1]:
           db.insertTrace(db.selectTraceWithName(nomTrace),i.attrib['lat'],i.attrib['lon'])

    def dataGpxToArray(self,idTrace):
        trace=[]
        requete = db.selectDataWithIdTrace(idTrace)
        for i in requete:
            trace.append(requete[i][0])
            trace.append(requete[i][1])
        return trace