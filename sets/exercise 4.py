#Exercise 4:set .add
n=int(raw_input()) #number of stamps
stamp=set([raw_input() for i in range(n)]) #add all the stamps to a list and convert it into a set
print len(stamp) #print the real number of stamps (no repetitions)