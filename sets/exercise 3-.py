#Exercise 3:No Idea!

raw_input()
st=raw_input().spilt() #take the list
A=set(raw_input().spilt()) #take the 'happy' set
B=set(raw_input().spilt()) #take the 'sad' set
score=0 

for i in st: #for each member of the list
    if i in A: #if i in A, add 1 point
        score+=1
    elif i in B: #if in B, remove 1 point (use 'elif', supposing that if one element is in A, cannot be in B)
        score-=1
print score

