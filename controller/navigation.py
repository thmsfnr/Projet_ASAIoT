
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
        if (((trace[0])>=(lat)-1.0) and ((trace[0])<=(lat)+1.0)) and (((trace[1])>=(lon)-1.0) and ((trace[1])<=(lon)+1.0)): #  The user is at minus 1 or plus 1 of the starting latitude and longitude of the trace
            res = True
        return res # Bool

    def isFinish(self,trace,lat,lon):
        """Return if the user has completed the trace"""

        res = False
        if ((trace[len(trace)-2]>=lat-0) and (trace[len(trace)-2]<=lat+0)) and ((trace[len(trace)-1]>=lon-0) and (trace[len(trace)-1]<=lon+0)): # The user is at minus 1 or plus 1 of the end latitude and longitude of the trace
            res = True
        return res # Bool

    def nextPoint(self,trace,lat,lon):
        """Return the next point of the trace relative to the current position"""

        res = []
        cpt = 2
        while (cpt<len(trace)-1) and (len(res)<4):
            if (float(lat)<=float(trace[cpt]) and float(lat)>=float(trace[cpt-2])) and (float(lon)<=float(trace[cpt+1]) and float(lon)>=float(trace[cpt-1])): # The user is located between these two latitudes and these two longitudes
                res.append(trace[cpt])
                res.append(trace[cpt+1])
            cpt += 2
        if len(res) == 0:
            res.append(trace[0])
            res.append(trace[1])
        return res # Array

    def speedToDistance(self,speedAvg,duration):
        """Calculate a distance with an average speed an a duration"""
        
        return speedAvg/duration

    def calcSpeedAvg(self,currentSpeed,prevSpeedAvg):
        """Calculate the current average speed"""

        return (currentSpeed+prevSpeedAvg)/2

    def indexMeter(self,distance,trace):
        """Find the current position"""
        
        res = 0
        cpt = 1
        while (cpt<len(trace)-1) and (res==0):
            if (distance<=trace[cpt]) and (distance<=trace[cpt+1]): 
                res = cpt
            cpt += 1
        return res

    def placeGpx(self,index,trace):
        """Find the latitude and longitude associated with an index"""

        res = []
        cpt = 2
        while (cpt<len(trace)-1) and (len(res)<2):
            if (cpt/2) == index: 
                res.append(trace[cpt])
                res.append(trace[cpt+1])
            cpt += 2
        return res 

    def directionTerminal(self,nextPoint,lat,lon,orientation):
        """Return the direction to follow to continue the trace"""
        """Nord = 0, East = 90, West = 270, South = 180"""
        
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
        """Return the direction to follow to continue the trace"""
        """Nord = 0, East = 90, West = 270, South = 180"""
        
        if (orientation>45) and (orientation<135):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(2) # tout droit
                else:
                    vibrer(4) # demi-tour
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    vibrer(6) # à droite
                else:
                    vibrer(5) # à gauche
        elif ((orientation>=0) and (orientation<=45)) or ((orientation>315) and (orientation<360)):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(5)
                else:
                    vibrer(6)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    vibrer(2)
                else:
                    vibrer(4)
        elif (orientation>=135) and (orientation<225):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(6)
                else:
                    vibrer(5)
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
                    vibrer(5)
                else:
                    vibrer(6)
    
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
        #print("Vous etes arrive")

    def directionWithoutGps(self,nextPoint,lat,lon,orientation,dist):
        """Return the direction to follow to continue the trace"""
        """Nord = 0, East = 90, West = 270, South = 180"""
        
        res = []
        if (orientation>45) and (orientation<135):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    res.append(2)
                else:
                    res.append(4)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    res.append(6)
                else:
                    res.append(5)
        elif ((orientation>=0) and (orientation<=45)) or ((orientation>315) and (orientation<360)):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    res.append(5)
                else:
                    res.append(6)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    res.append(2)
                else:
                    res.append(4)
        elif (orientation>=135) and (orientation<225):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    res.append(6)
                else:
                    res.append(5)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    res.append(4)
                else:
                    res.append(2)
        elif (orientation>=225) and (orientation<=315):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    res.append(4)
                else:
                    res.append(2)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    res.append(5)
                else:
                    res.append(6)

    def navigationWithoutGps(self,trace):
        """Full navigation management without gps"""

        dist = 0
        """
        while (dist <= lengthTrace(trace)):
            orientation=getOrientation()
            pos = self.placeGpx(self.indexMeter(dist,trace))
            nextPoint = self.nextPoint(trace,pos[0],pos[1])
            direction = self.directionWithoutGps(nextPoint,pos[0],pos[1],orientation,dist)
            if """
            


        # Tant que dist n'est pas égale à la longeur de la trace
            # obtenir point suivant
            # obtenir direction
