#Exercise 6:Collections.deque()
from collections import deque

l=deque() #create the deque

for i in xrange(input()): 
    c=raw_input().split() #split the input
    if len(c)== 2: #if the input conteins the method name and a value, find and use that method
        getattr(l,c[0])(c[1])
    elif len(c)==1:       #otherwise, if it conteins only the method, do the same
        getattr(l,c[0])()
        
print ' '.join(l) #print all the current elements,present into l 