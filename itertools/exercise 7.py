# Exercise 7: maximize it!

import itertools

sts, D= map(int, raw_input().split()) #take the number of sets and the divisor
l=[] #empty list, to append the sets

for i in xrange(sts): 
    s=map(int,raw_input().split()[1:]) #take the set(to avoid repetitions), removing the first element
    s=set(itertools.imap(pow, s, itertools.repeat(2))) #compute the square of each element
    l.append(s) #append to l
    
comb=map(list,itertools.product(*l)) #compute all the possible combinations
print max([sum(j)%D for j in comb]) #print the maximum rest among all the possible combinations