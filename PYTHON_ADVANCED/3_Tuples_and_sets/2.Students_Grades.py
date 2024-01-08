n = int(input())

students = {}

for _ in range(n):
    
    student = input().split()

    if student[0] in students:

        students[student[0]].append(float(student[1]))

    else:
        
        students[student[0]] = []
        students[student[0]].append(float(student[1]))

for key, value in students.items():
    
    formatted_grades = ' '.join([f"{grades:.2f}" for grades in value])
    print(f"{key} -> {formatted_grades} (avg: {sum(value) / len(value):.2f})")