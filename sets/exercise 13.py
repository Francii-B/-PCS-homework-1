#Exercise 13: Check String Superset

A = set(raw_input().split()) #superset
a=set()                      #create a set conteining 1 if the subset is not in A and 0 otherwise 
for i in range(int(raw_input())): #for loop is repeated as many time as the number of subset 
    Subset = set(raw_input().split())  #read the current subset
    if((A&Subset)==set(Subset)):       #if the common elements between A and the subset are the same in the subset...
        a.add(1)     #add 1
    else:
        a.add(0)   #otherwise 0
print not(0 in a) #if a subset is not in A, return False


    