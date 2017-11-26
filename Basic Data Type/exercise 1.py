#Exercise 1:Lists
if __name__ == '__main__':
    N = int(raw_input())
    input_l=[]  # create a List where the commands will be inserted
    l=[]        # empty list 
    for N in range(N):
        c= raw_input().split(" ") #insert commands into the list, by divinding each element (strings)
    
        if c[0]=="insert": #the first element of c express the command
            l.insert(int(c[1]), int(c[2])) #Constraints: The elements added to the list must be integers.
        
        elif c[0]== "print":
            print l          
          
        elif c[0]== "remove":
            l.remove(int(c[1]))
        
        elif c[0]== "append":
            l.append(int(c[1]))
        
        elif c[0]== "sort":
            l.sort()
           
        elif c[0]== "reverse":
            l.reverse()
        
        elif c[0]== "pop":
            l.pop(-1)