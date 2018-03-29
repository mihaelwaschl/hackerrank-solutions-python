n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

num = student_marks[query_name]
sumGrades = 0
for i in num:
    sumGrades += i
avarage = sumGrades/len(num)
print('{:.2f}'.format(avarage))
