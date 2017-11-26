# Exercise 2: itertool.permutations()
import itertools 

inp=raw_input().split() #take the string

for i in itertools.permutations(sorted(inp[0]), int(inp[1])): #for each permutation (composed by inp[1]-elements)...
    print ''.join(i) #join it together (strings) 