n = int(input("Enter no.of.students:"))
students_marks={}
for i in range(n):
    name, *line = input("Enter name").split()
    scores = list(map(float, line))
    students_marks[name] = scores
query_name = input("Enter query name:")
for i in students_marks:
    if i==query_name:
        total=sum(students_marks[i])
        avg=total/len(students_marks[i])
        print("%.2f"%avg)
