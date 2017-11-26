#Exercise 4:Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:] #slice the string and insert the character in the required position