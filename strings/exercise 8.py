#Exercise 8: text wrap
import textwrap   #import the module

def wrap(string, max_width):
    return textwrap.fill(string,max_width) #wrap the string to return a new string