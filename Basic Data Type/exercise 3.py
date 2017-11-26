#Exercise 3= List comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    if (x | y | z) < 0:  #the coordinates x,y and z must be greater or equal to 0
        print "wrong coordinates"
    else:
        print [ [ i, j, m] for i in range( x + 1) for j in range( y + 1) for m in range(z+1) if ( ( i + j+ m ) != n )]
    
    #each combination is established by a for-cicle for each integers (X,Y,Z). Their sum must be different from n
    #the combinations are already sorted 