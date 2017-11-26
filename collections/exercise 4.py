#Exercise 4: collections.OrderedDict()
from collections import OrderedDict


Prize=OrderedDict()

for i in xrange(input()): #for each element and its prize
    inp=raw_input().rsplit(' ',1) #record the name and prize (split into two parts)
    if inp[0] in Prize: #If the element is already in the dictionary, just modify it
        Prize[inp[0]]+=int(inp[-1])
    else:
        Prize[inp[0]]=int(inp[-1]) #otherwise record it 

for j in Prize: #for each element (sorted by entering order)
    print j +' '+ str(Prize[j]) #print the name, and the net prize 
    