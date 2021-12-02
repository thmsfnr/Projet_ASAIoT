import time
from useSensors import *

class nav:

    def init():
        """Initialisation of the nav"""

        print("OK")

    def canStart(self,trace,lat,lon):
        """Return if the navigation can start"""

        res = False
        if ((trace[0]>=lat-1) and (trace[0]<=lat+1)) and ((trace[1]>=lon-1) and (trace[1]<=lon+1)): #  The user is at minus 1 or plus 1 of the starting latitude and longitude of the trace
            res = True
        return res # Bool

    def isFinish(self,trace,lat,lon):
        """Return if the user has completed the trace"""

        res = False
        if ((trace[len(trace)-2]>=lat-1) and (trace[len(trace)-2]<=lat+1)) and ((trace[len(trace)-1]>=lon-1) and (trace[len(trace)-1]<=lon+1)): # The user is at minus 1 or plus 1 of the end latitude and longitude of the trace
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
        return res # Array

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
                    vibrer(3) # à droite
                else:
                    vibrer(4) # à gauche
        elif ((orientation>=0) and (orientation<=45)) or ((orientation>315) and (orientation<360)):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(4)
                else:
                    vibrer(3)
            else:
                if (float(lon)-float(nextPoint[1])) < 0:
                    vibrer(2)
                else:
                    vibrer(4)
        elif (orientation>=135) and (orientation<225):
            if abs(float(lat)-float(nextPoint[0])) > abs(float(lon)-float(nextPoint[1])):
                if (float(lat)-float(nextPoint[0])) < 0:
                    vibrer(3)
                else:
                    vibrer(4)
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
                    vibrer(4)
                else:
                    vibrer(3)
    
    def navigation(self,trace):
        """Full navigation management"""

        lat=0
        lon=0
        orientation=0
        while (self.isFinish(trace,lat,lon) == False): # The user has not completed the trace
            pointSuivant = self.nextPoint(trace,lat,lon)
            nav2i = self.direction(pointSuivant,lat,lon,orientation)
            print(nav2i) # Direction to follow
            time.sleep(2)
            lat=0
            lon=0
            orientation=getOrientation()
        print("Vous etes arrive")





