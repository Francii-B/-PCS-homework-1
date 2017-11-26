#Exercise 6: String Validationo
if __name__ == '__main__':
    s = raw_input()
    print any([c.isalnum() for c in s]) #check each member of the string by different methods. If at least one member returns True, then return True
    print any([c.isalpha() for c in s])
    print any([c.isdigit() for c in s])
    print any([c.islower() for c in s])
    print any([c.isupper() for c in s])