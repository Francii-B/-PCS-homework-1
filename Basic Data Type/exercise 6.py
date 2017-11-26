#Exercise 6: Finding the percentage
if __name__ == '__main__':
    n = input()
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    if query_name in student_marks: #if the query_name is in the dictionary
        summ=sum(student_marks[query_name]) #sum all the scores
        print format(summ/3, '.2f') #and then find the average( the result is rounded to 2 decimals places)