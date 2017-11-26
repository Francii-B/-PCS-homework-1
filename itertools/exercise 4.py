# Exercise 4: itertools.combinations_with_replacement

import itertools

word,ln=raw_input().split() #take the string and the lenght of the combinations

for i in itertools.combinations_with_replacement(sorted(word), int(ln)): #for each combination with replacement, of ln-lenght...
    print ''.join(i) #join it together (strings)