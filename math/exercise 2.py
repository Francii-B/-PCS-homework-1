# -*- coding: utf-8 -*-
#Exercise 2: Find Angle MBC
import math

y=(input()/2.0) #take the y coordinate of M(half of AB) 
x=(input()/2.0) #take the x coordinate of M(half of BC) 
angle=round(math.degrees(math.atan(y/x))) # arctangent of the slope corresponds to the angle MBC. round the angle (already converted to degrees)

print str(angle)[:-2] + "°" #print the angle(no decimal numbers)