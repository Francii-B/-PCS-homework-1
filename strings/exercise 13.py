#Exercise 13:Minion
def minion_game(string):
    spoints, kpoints= 0, 0 #create the two scores
    
    for i in range(len(string)): #for each letter in the world...
            if string[i] in 'AEIOU': #...if the initial letter of the substring is a vowel... 
#line 7 and 8 are taken from discussions
                kpoints+=len(string)-i #add the number of all possible combinations of sub-string to the kevin's scores
            else:
                spoints+=len(string)-i #otherwise add them to the stuart's scores 
    
    if kpoints<spoints: #print the name and the score of the winner
        print "Stuart "+ str(spoints)
    elif kpoints>spoints:
        print "Kevin " + str(kpoints)
    else:
        print "Draw"
        
        
        

