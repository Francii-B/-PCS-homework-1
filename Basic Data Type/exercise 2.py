#Exercise 2: Tuple
if __name__ == '__main__':
    input()
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))  #Convertion of the list into a tuple, and then, compute the hash value for the tuple