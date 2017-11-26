#Exercise 11: Alphabet Rangoli
def print_rangoli(size):
    rangoli=[]
    
    for i in xrange(size):
        ran=[chr(ord('a')+size-1-l) for l in range(i+1)] #write all the letters present in a line of the alp.rangoli
        written='-'.join(ran[:-1]+ran[::-1]) #join the letters together(divided by '-')
        rangoli.append(written.center(4*size-3, "-")) #append the final line(the written is in the center of the line) to the list 'rangoli'
        
    print '\n'.join(rangoli[:-1]+rangoli[::-1]) #print the upper-part(except for central line, to avoid repetitions) and the bottom part(including the central line)
        