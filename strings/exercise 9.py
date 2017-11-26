#Exercise 9: Designer Door Mat

N, M = map(int,raw_input().split()) 

for i in xrange(1,N,2): # upper part of the door
    print (i*".|.").center(M, "-") # center the written ".|."; every time ".|." duplicate itself, forming a triangle

print "WELCOME".center(M, "-") # central written

for i in xrange(N-2,-1,-2):  # bottom part of the door
    print (i*".|.").center(M, "-") # same as upper part, but the triangle is up-side-down