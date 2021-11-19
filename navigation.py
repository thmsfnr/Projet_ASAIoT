import time

class nav:

    def init():
        """Initialisation of the nav"""

        print("OK")

    def canStart(self,trace,lat,lon):
        """Return if the navigation can start"""

        res = False
        if ((trace[0]>=lat-1) and (trace[0]<=lat+1)) and ((trace[1]>=lon-1) and (trace[1]<=lon+1)):
            res = True
        return res

    def isFinish(self,trace,lat,lon):
        

        res = False
        if ((trace[len(trace)-2]>=lat-1) and (trace[len(trace)-2]<=lat+1)) and ((trace[len(trace)-1]>=lon-1) and (trace[len(trace)-1]<=lon+1)):
            res = True
        return res

    def nextPoint(self,trace,lat,lon):
        res = []
        cpt = 2
        while (cpt<len(trace)-1) and (len(res)<4):
            if (float(lat)<=float(trace[cpt]) and float(lat)>=float(trace[cpt-2])) and (float(lon)<=float(trace[cpt+1]) and float(lon)>=float(trace[cpt-1])):
                res.append(trace[cpt])
                res.append(trace[cpt+1])
            cpt += 2
        return res

    def direction(self,nextPoint,lat,lon,orientation):
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
                    return("a gauche")
                else:
                    return("a droite")
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
    
    def navigation(self,trace):
        lat=0
        lon=0
        orientation=0
        while (self.isFinish(trace,lat,lon) == False):
            pointSuivant = self.nextPoint(trace,lat,lon)
            nav2i = self.direction(pointSuivant,lat,lon,orientation)
            print(nav2i)
            time.sleep(2)
            lat=0
            lon=0
            orientation=0
        print("Vous etes arrive")





