#Exercise 4: Find the Second Largest Number 
if __name__ == '__main__':
    input() 
    arr = set(map(int, raw_input().split())) #store the numbers in a list and convert it into a set (to avoid repetitions)
    arr.remove(max(arr))  #remove the highest value
    print max(arr) #print the second highest value
