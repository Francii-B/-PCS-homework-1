# Exercise 5:Compress the string
from __future__ import print_function #import print function
import itertools

for n,l in itertools.groupby(raw_input(), int): #n corresponds to the element of the sequence of numbers, while l corresponds to the repetitions
    print((n,len(list(l))) , end=' ') #print the tuples, separated by a space
    