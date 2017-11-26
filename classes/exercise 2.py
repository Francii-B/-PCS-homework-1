# Exercise 2:Find the torsional angle
import math as m

class Points(object):
    def __init__(self, x, y, z): #initialize the class
        self.x, self.y, self.z= float(x), float(y),float(z)

#For better understanding, suppose
#'self.' vector: A(x,y,z)
#'no.' vector: B(X,Y,Z)        
                        
    def __sub__(self, no): #subtraction between two vectors
        x=self.x-no.x
        y=self.y-no.y
        z=self.z-no.z
        return Points(x,y,z)
        
    def cross(self, no): #cross product 
        x=(self.y*no.z)-(no.y*self.z) #(y*Z)-(Y*z)
        y=(self.z*no.x)-(no.z*self.x) #(z*X)-(Z*x)
        z=(self.x*no.y)-(no.x*self.y) #(x*Y)-(y*Y)
        return Points(x,y,z)

    def dot(self, no): #dot product
        return (self.x*no.x)+(self.y*no.y)+(self.z*no.z) #(x*X)+(y*Y)+(z*Z)
        
    def absolute(self): #lenght of the vector
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)