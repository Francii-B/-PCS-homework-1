# Exercise 2:defaultDic tutorial
from collections import defaultdict


A,B=map(int,raw_input().split()) # take the lenght of the two groups
A_dict= defaultdict(list) #create the dictionary A
B_lst=[] #create a list B

for i in range(A+B): #repeat the input for each input    
    if i<A:     #if i-input belongs to the A group, append it's position 
        A_dict[raw_input()].append(i+1)       
   
    else:      #if the input belongs to the B group,chek if it is present in A
        el=raw_input()
        if el in A_dict:
            B_lst.append( ' '.join(map(str,A_dict[el])))
        else: #otherwise add -1 to the list
            B_lst.append(-1)
            
for j in B_lst: #print all the occurrences
    print j
