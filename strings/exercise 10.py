#Exercise 10: String Formatting

def print_formatted(number):
    space=len(format(number,'b'))+1 #establish the space between numbers equal to the lenght of binary value of 'number' plus 1
    
    for i in xrange(1,number+1):   #cyclically converts all the number between 1 and 'number'
        print str(i).rjust(space-1)+format(i,'o').rjust(space)+((format(i,'x').upper())).rjust(space)+format(i,'b').rjust(space) 
                                    #add 'space' before writing each value