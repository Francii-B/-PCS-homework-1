# Exercise 1:collections.Counter()
import collections

input()
shoes=collections.Counter(raw_input().split()) #take all the sizes
money=0 #initial incoming

for i in range(input()): #repeat the loop as the number of sold sizes
    size, prize=raw_input().split() #take the size and the prize
    
    if shoes[size] != 0: #if the size is still present (value of key different from 0)....
        shoes[size]-=1   #decrease the number of size left in the shop
        money+=int(prize) #add the prize of the shoe to the incoming money

print money #print the total incoming