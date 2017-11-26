# Exercise 1: Classes: Dealing with Complex Numbers
import math 

class Complex(object):
    def __init__(self, real, imaginary): # initialization of the new Complex element 
        self.real, self.imaginary= real, imaginary

# Suppose that the 'self.' element is Z=A+Bi, while the 'no.' is W=C+Di
        
    def __add__(self, no): # addiction 
        num=Complex(self.real+ no.real,self.imaginary+ no.imaginary)#real=A+C, imaginary=B+D
        return num.__str__() #print in the required manner, using the method '__str__()'
    
    def __sub__(self, no): #subtraction 
        num=Complex(self.real- no.real,self.imaginary-no.imaginary)#real=A-C, imaginary=B-D
        return num.__str__()    
        
    def __mul__(self, no): #multiplication between
        re=(self.real* no.real)-(self.imaginary*no.imaginary) #real=(AC-BD) 
        im=(self.real* no.imaginary)+(no.real* self.imaginary)# imaginary=(CB+DA)
        num=Complex(re, im)
        return num.__str__()
        
    def __div__(self, no):
        re=(self.real* no.real)+(self.imaginary*no.imaginary)#real=(AC+BD) 
        im=(no.real* self.imaginary)-(self.real* no.imaginary)# imaginary=(CB-DA)
        den=float(no.real**2+no.imaginary**2) # denominator=(C^2+D^2)
        num=Complex(re/den, im/den)
        return num.__str__()
        
    def mod(self): #module
        num=Complex((self.real**2+self.imaginary**2)**0.5,0) # module=sqrt(A^2+B^2)
        return num.__str__()

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result