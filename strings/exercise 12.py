#Exercise 12: capitalize

def capitalize(string):
    cap=[]
    
    for i in string.split(" "): #split the string and start a for-loop ('i' assumes eache element of the splitted string)
        if len(i)!=0 and i[0].isalpha: #if the element is not empty and the first letter is alphabetic....
            i=i.capitalize()   #...capitalize the word
        cap.append(i) #appent the element to the new list
   
    return ' '.join(cap) #return the joined-new list( as a string)
    
