#Exercise 2:Symmetric Differences

raw_input()
s1=map(int,raw_input().split()) #take the first sequence of numbers, split them, and convert them in integer numbers
raw_input()
s2=map(int,raw_input().split()) #same for the second sequence

for i in sorted(set(s1)^set(s2)): #for each element in the sorted set of uncommon value
    print i                     #print each one