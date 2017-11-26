# Exercise 7: Piling Up!
    
for i in xrange(input()):    # repeat the process for n-times
    input()       # lenght of the cubes
    cubes=map(int,raw_input().split())  # list of cubes
    minim=cubes.index(min(cubes))      # find the minimum value, and find it's position
    a, b= cubes[:minim], cubes[minim:]   # divide the list into two sublist 
    
    if a== sorted(a,reverse=True) and b==sorted(b): # if both lists are already sorted, print Yes
        print 'Yes'
    else:   # otherwise print No 
        print 'No'