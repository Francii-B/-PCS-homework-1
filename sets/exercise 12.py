#Exercise 12: Check Subset
for i in range(int(raw_input())):  
    a = int(raw_input()); A = set(raw_input().split()) 
    b = int(raw_input()); B = set(raw_input().split())
    if (b>=a) and ((A&B)==A): #if the set A is smaller than B and the common elemnts corresponds to the set A
        print True          #A is a subset of B
    else:
        print False         #otherwise it's not a subset of B