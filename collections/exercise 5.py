#Exercise 5:Word Order
from collections import OrderedDict


w_ord=OrderedDict()

for i in xrange(input()): #for each word
    inp=raw_input() #record the it
    if inp in w_ord: #If the element is already in the dictionary, just add one (1 more occurrence)
        w_ord[inp]+=1
    else:
        w_ord[inp]=1 #otherwise record it , and it's value is 1 (meaning only one occurrence)
        
print len(w_ord) #print the number of distinct elements
print ' '.join(map(str,w_ord.values())) #print all the occurrences
    