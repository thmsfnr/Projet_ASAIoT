import xml.etree.ElementTree as ET

def GpxToArray(file):
    trace=[]
    tree = ET.parse(file)
    root = tree.getroot()
    #return("L'element racine : ", root.tag)
    #return("Le premier enfant de la racine : ", root[1][1].tag)
    for a in root[1][1]:
        trace.append(a.attrib['lat'])
        trace.append(a.attrib['lon'])
    return trace