#Exercise 6:Set .union()

raw_input()
Eng=set(raw_input().split()) #take the roll number of students who have subscribe the English newpaper
raw_input()
Fre=set(raw_input().split()) #the same with the French newpaper
print len(Eng|Fre)          #combine the two sets(excluding repetitions), printing the lenght of the new set