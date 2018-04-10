from collections import namedtuple

numStudents = int(input())
students = namedtuple('Students',input().split())
sum = 0
for i in range(0,numStudents):
    id, marks, name, clas = input().split()
    table = students(id, marks,  name, clas)
    sum += int(table.MARKS)
print('{:.2f}'.format(sum/numStudents))