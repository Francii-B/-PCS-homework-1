#Exercise 5: Nested Lists 
students=[]
s=set()     #create a list and a set

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score]) #append name and score as sub-list 
    s.add(score)  #add the scores to the set
    
s.remove(min(s))  #remove the smallest score

for i,j in sorted(students):
    if j==min(s): #print the name of the student if the score corresponds to the new smallest score
        print i