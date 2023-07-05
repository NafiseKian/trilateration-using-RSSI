import math
from math import sin, cos, sqrt, atan2, radians, pi
import pandas as pd
import csv
from math import pow
import numpy as np
import matplotlib.pyplot as plot


dist_arr_1=[1.413 , 1.0 , 0.891 , 1.585 , 0.794 , 1.0 , 0.891 , 0.794]
dist_arr_2=[1.112 , 1.010 , 0.554 , 0.674 , 0.810 , 0.443 , 0.421 , 0.932]
dist_arr_3=[0.178 , 0.178 , 0.282 , 0.178 , 0.282 , 0.178 , 0.056 , 0.04]




mean_1=np.nanmean(dist_arr_1)
mean_2=np.nanmean(dist_arr_2)
mean_3=np.nanmean(dist_arr_3)

print("distance from point 1=",mean_1)
print("distance from point 2=",mean_2)
print("distance from point 3=",mean_3)

  
def trilateration(x1,y1,r1,x2,y2,r2,x3,y3,r3):
    
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    ex = [(x2 - x1) / d, (y2 - y1) / d]

    
    i = [ex[0] * (x3 - x1), ex[1] * (y3 - y1)]

    
    ey = [(x3 -x1 - i[0] * ex[0]) / math.sqrt((x3 - x1 - i[0] * ex[0])**2 + (y3 - y1- i[1] * ex[1])**2),(y3- y1 - i[1] * ex[1]) / math.sqrt((x3 - x1 - i[0] * ex[0])**2 + (y3 - y1 - i[1] * ex[1])**2)]

    
    j = [ey[0] * (x3 - x1), ey[1] * (y3 -y1)]

    
    x = (r1**2 - r2**2 + d**2) / (2 * d)

    
    y = (r1**2 - r3**2 + i[0]**2 + i[1]**2 + j[0]**2 + j[1]**2) / (2 * j[0]) - (i[0]) / j[0]

    return x,y

x,y = trilateration(1.1,1,mean_1,1,3,mean_2,3,0,mean_3)

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  
print("distance between calculated and center(0,0)=", calculateDistance(0, 0, x, y) ) 

print("calculated coordinates of tag (x,y)=",x,y)
