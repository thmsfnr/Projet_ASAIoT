import xml.etree.ElementTree as ET
from interactionDB import DB

class GPX:
    
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
        DB.insertTrace(nomTrace)
        tree = ET.parse(file)
        root = tree.getroot()
        for i in root[1][1]:
           DB.insertTrace(DB.selectTraceWithName(nomTrace),i.attrib['lat'],i.attrib['lon'])

    def dataGpxToArray(self,idTrace):
        trace=[]
        requete = DB.selectDataWithIdTrace(idTrace)
        for i in requete:
            trace.append(requete[i][0])
            trace.append(requete[i][1])
        return trace