#Exercise 8: Most Common
from collections import Counter

occ=Counter(raw_input())  #take the string

for i in xrange(3): #build the top-three
    el=max(sorted(occ.items()),key=lambda k: k[1]) #record the most repeated letter, basing on the number of occurrences
    print el[0]+ ' ' +  str(el[1]) #print the result
    del occ[el[0]] #and delete it from the dictionary 