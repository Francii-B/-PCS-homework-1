# Exercise 3: itertools.combinations()
import itertools

inp=raw_input().split() #take the string and the max lenght of combinations

for j in range(1,int(inp[1])+1): #loop for the lenght of combinations
    
    for i in itertools.combinations(sorted(inp[0]),j): #for each combination
        print ''.join(i) #join together its elements
 