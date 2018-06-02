num_students, num_subject = map(int,input().split())
subjects = []

for i in range(num_subject):
    subjects.append([float(x) for x in input().split()])

for j in zip(*subjects):
    print(sum(j)/num_subject)

