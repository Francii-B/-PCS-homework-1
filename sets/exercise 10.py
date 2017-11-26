#Exercise 10:Set Mutations

raw_input()
data=set(raw_input().split())   #take the original set (split the numbers, and covert the list into a set)
lcom=xrange(int(raw_input()))   #number of inputs
for i in lcom:                 #for each input...
    com=raw_input().split()     #take the command
    mod=set(raw_input().split()) #and take the second set (called 'mod')
    if com[0]== 'update':       #if the command is update, add 'mod' to the original set ('data')
        data|=mod
    elif com[0]== 'difference_update': 
        data-=mod                      #remove from data the common elements with mod
    elif com[0]== 'symmetric_difference_update':
        data^=mod                     #remove all the common elements between data and mod
    elif com[0]== 'intersection_update':
        data&=mod                   #mantein the common element of data with mod
print sum(map(int,data))           #convert the element of data into integers, and sum them