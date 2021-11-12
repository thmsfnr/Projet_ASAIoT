import xml.etree.ElementTree as ET

def GpxToArray(file):
    trace=[]
    tree = ET.parse(file)
    root = tree.getroot()
    #print("L'element racine : ", root.tag)
    #print("Le premier enfant de la racine : ", root[1][1].tag)
    for a in root[1][1]:
        trace.append(a.attrib['lat'])
        trace.append(a.attrib['lon'])
    return trace

def encadrement(trace,lat,lon):
    res = []
    cpt = 2
    while (cpt<len(trace)-1) and (len(res)<4):
        if (float(lat)<float(trace[cpt]) and float(lat)>float(trace[cpt-1])) and (float(lon)<float(trace[cpt]) and float(lon)>float(trace[cpt-1])):
            #res.append(trace[cpt-2])
            #res.append(trace[cpt-1])
            res.append(trace[cpt])
            res.append(trace[cpt+1])
        cpt += 2
    return res

def direction(pointSuivant,lat,lon,orientation):
    if (orientation>45) and (orientation<135):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                print("tout droit")
            else:
                print("demi-tour")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                print("a droite")
            else:
                print("a gauche")
    elif ((orientation>=0) and (orientation<=45)) or ((orientation>315) and (orientation<360)):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                print("a droite")
            else:
                print("a gauche")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                print("tout droit")
            else:
                print("demi-tour")
    elif (orientation>=135) and (orientation<225):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                print("a gauche")
            else:
                print("a droite")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                print("demi-tour")
            else:
                print("tout droit")
    elif (orientation>=225) and (orientation<=315):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                print("demi-tour")
            else:
                print("tout droit")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                print("a gauche")
            else:
                print("a droite")





