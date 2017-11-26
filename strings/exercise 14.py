#Exercise 14:Merge the tools

def merge_the_tools(string, k):
    for i in xrange(0,len(string),k): #divide the string into k-long substring
        word=''                        #create the new string that contains the content of the substring, without repetitions
        
        for el in string[i:i+k]:      #for each element in the substring...
            if el not in word:        #if the element is not already present in 'word', add it
                word+=el 
        print word                  #print the output(substring without repetitions)