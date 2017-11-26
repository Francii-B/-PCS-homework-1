# Exercise 3: Collections.nametuple()
from collections import namedtuple

students=input()#take the number of students
r =namedtuple('r',raw_input().split())  # take the student's informations 

summ=sum([float(r(*raw_input().split()).MARKS) for i in xrange(students)]) #for each student, extract the Mark, and sum all together

print summ/students #print the avarage

#additional challange: write 4 line code.

