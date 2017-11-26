#Exercise 5:Set .discard(), .remove() & .pop()
n=raw_input()                           #take the len of the set
data=set(map(int, raw_input().split())) #take the set
lcom=xrange(int(raw_input()))           #take the number of inputs
for i in lcom:                         # for each command...
    com=raw_input().split(" ")         #take the command and plit it into two parts: command and number(position or member of 'data')
    if len(data)!=0:
        if com[0]=="pop":            #if the first element of 'com' is pop, it removes an element
            data.pop()               
        elif com[0]== "discard" or com[0]=="remove": #if the command is discard or remove, it removes the com[1]-specific element
            data.discard(int(com[1]))
print sum(data) #sum the remaining elements in 'data'

