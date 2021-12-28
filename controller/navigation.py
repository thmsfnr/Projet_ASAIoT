
import sys  
from pathlib import Path  
file = Path("navigation.py").resolve()  
package_root_directory = file.parents[1]  
sys.path.append(str(package_root_directory))  

import time
from controller.useSensors import *

class nav:

    def init():
        """Initialisation of the nav"""

        print("OK")

    def canStart(self,trace,lat,lon):
        """Return if the navigation can start"""

        res = False
        if (((trace[0])>=(lat)-0.002) and ((trace[0])<=(lat)+0.002)) and (((trace[1])>=(lon)-0.002) and ((trace[1])<=(lon)+0.002)): #  The user is at minus 1 or plus 1 of the starting latitude and longitude of the trace
            res = True
        return res # Bool

    def isFinish(self,trace,lat,lon):
        """Return if the user has completed the trace"""

        res = False
        if ((trace[len(trace)-2]>=lat-0.0001) and (trace[len(trace)-2]<=lat+0.0001)) and ((trace[len(trace)-1]>=lon-0.0001) and (trace[len(trace)-1]<=lon+0.0001)): # The user is at minus 1 or plus 1 of the end latitude and longitude of the trace
            res = True
        return res # Bool

    def nextPoint(self,trace,lat,lon):
        """Return the next point of the trace relative to the current position"""

        res = []
        cpt = 2
        while (cpt<len(trace)-1) and (len(res)<4):
            if (((lat)>=(trace[cpt]) and (lat)<=(trace[cpt-2])) or ((lat)<=(trace[cpt]) and (lat)>=(trace[cpt-2]))) and (((lon)>=(trace[cpt-1]) and (lon)<=(trace[cpt+1])) or ((lon)<=(trace[cpt-1]) and (lon)>=(trace[cpt+1]))): # The user is located between these two latitudes and these two longitudes
                res.append(trace[cpt])
                res.append(trace[cpt+1])
                print("ok")
            elif (((lat)>=(trace[cpt]) and (lat)<=(trace[cpt-2])) or ((lat)<=(trace[cpt]) and (lat)>=(trace[cpt-2]))) and ((((lon)<=(trace[cpt+1])+0.01) and ((lon)>=(trace[cpt-1])-0.01)) or (((lon)>=(trace[cpt+1])-0.01) and ((lon)<=(trace[cpt-1])+0.01))):
                res.append(trace[cpt])
                res.append(trace[cpt+1])
                print("ok1")
            elif (((lon)>=(trace[cpt-1]) and (lon)<=(trace[cpt+1])) or ((lon)<=(trace[cpt-1]) and (lon)>=(trace[cpt+1]))) and ((((lat)<=(trace[cpt])+0.01) and ((lat)>=(trace[cpt-2])-0.01)) or (((lat)>=(trace[cpt])-0.01) and ((lat)<=(trace[cpt-2])+0.01))):
                res.append(trace[cpt])
                res.append(trace[cpt+1])
                print("ok2")
            cpt += 2
        if len(res) == 0:
            res.append(trace[0])
            res.append(trace[1])
        return res # Array

    def directionTerminal(self,nextPoint,lat,lon,orientation):
        """Return the direction to follow to continue the trace in the terminal"""
        
        # Nord = 0, East = 90, West = 270, South = 180
        
        if (orientation>45) and (orientation<135):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    return("tout droit")
                else:
                    return("demi-tour")
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    return("a droite")
                else:
                    return("a gauche")
        elif ((orientation>=0) and (orientation<=45)) or ((orientation>315) and (orientation<360)):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    return("a gauche")
                else:
                    return("a droite")
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    return("tout droit")
                else:
                    return("demi-tour")
        elif (orientation>=135) and (orientation<225):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    return("a droite")
                else:
                    return("a gauche")
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    return("demi-tour")
                else:
                    return("tout droit")
        elif (orientation>=225) and (orientation<=315):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    return("demi-tour")
                else:
                    return("tout droit")
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    return("a gauche")
                else:
                    return("a droite")
    
    
    def direction(self,nextPoint,lat,lon,orientation):
        """Return the direction to follow to continue the trace with the vibrators"""
        
        # Nord = 0, East = 90, West = 270, South = 180
        
        if (orientation>45) and (orientation<135):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(2) # tout droit
                else:
                    vibrer(4) # demi-tour
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    vibrer(5) # à droite
                else:
                    vibrer(6) # à gauche
        elif ((orientation>=0) and (orientation<=45)) or ((orientation>315) and (orientation<360)):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(6)
                else:
                    vibrer(5)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    vibrer(2)
                else:
                    vibrer(4)
        elif (orientation>=135) and (orientation<225):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(5)
                else:
                    vibrer(6)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    vibrer(4)
                else:
                    vibrer(2)
        elif (orientation>=225) and (orientation<=315):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(4)
                else:
                    vibrer(2)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    vibrer(6)
                else:
                    vibrer(5)
    
    def navigation(self,trace):
        """Full navigation management"""

        lat=position()[0]
        lon=position()[1]
        orientation=getOrientation()
        while (self.isFinish(trace,lat,lon) == False): # The user has not completed the trace
            print(lat)
            print(lon)
            print(trace)
            print(orientation)
            pointSuivant = self.nextPoint(trace,lat,lon)
            print(pointSuivant)
            nav2i = self.direction(pointSuivant,lat,lon,orientation)
            print(nav2i) # Direction to follow
            time.sleep(2)
            lat=position()[0]
            lon=position()[1]
            orientation=getOrientation()
        print("Vous etes arrive")
