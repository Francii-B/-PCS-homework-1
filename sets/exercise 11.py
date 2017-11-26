#Exercise 11:The Captain's room

k=int(raw_input()) #take the number of members for each room (except the captain's one)
ppl=map(int,raw_input().split()) #take the room number for each person

hyp_members=sum(set(ppl))*k  #convert all the room numbers into a set,moltiply by k (result= k-elements for each room, also for Captain's room) and sum

print ((hyp_members-sum(ppl))/(k-1))  #the sum of excessive members of the captain's room  are divided by k-1(members-captain)  
        #result=captain room