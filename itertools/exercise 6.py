# Exercise 6: Iterables and iterators
import itertools

input() 
lett=raw_input().split() #take the sequence of lower-case letters
k=input() #lenght of combinations

com= list(itertools.combinations(lett, k)) #find all the possible combinations 
aa=list(itertools.ifilter(lambda x: 'a' in x, com)) #take only the ones which conteins 'a' (favorable cases)

print len(aa)/float(len(com)) #find the probability 
