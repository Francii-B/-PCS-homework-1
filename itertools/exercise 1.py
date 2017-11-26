#Exercise 1:itertools product()

import itertools 

A=map(int,raw_input().split()) #take the list A
B=map(int,raw_input().split()) #take the list B

print ' '.join(map(str,itertools.product(A,B))) #compute the cartesian product and join all the tuples