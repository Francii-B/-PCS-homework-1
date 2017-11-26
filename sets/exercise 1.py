#Exercise 1:Introduction to sets

def average(array):
    s=set(array[1:]) #convert array into a set 
    return float(sum(s))/len(s) #compute the average (lenght and sum is given by s) 
                                 # 'float' must be included if I want a float number as result in python 2.7 