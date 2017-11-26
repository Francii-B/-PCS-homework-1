#Exercise 5: Loops

if __name__ == '__main__':
    n = int(raw_input())
    if n<1 or n>20:         #Constraints: n must be included between 1 and 20
        print "not valid integer"
    else:
        for i in range(n):
            print i*i