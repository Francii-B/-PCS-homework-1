#Exercise 5:Find a string

def count_substring(string, sub_string):
    occ=0 #number of occurrences
    
    for i in xrange(len(string)):
        if string[i:len(sub_string)+i]==sub_string: #check if the string conteins the substring, position by position
            occ+=1 #if it present, occ increase by 1
            
    return occ #return the total number of occurrences