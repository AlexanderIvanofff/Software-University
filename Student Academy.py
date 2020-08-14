from collections import defaultdict

n = int(input())

data = defaultdict(list)
for i in range(n):
    student_name = input()
    grade = float(input())

    data[student_name] += [grade]


average_grade = {}

for kay, value in data.items():
    average = sum(value) / len(value)
    average_grade[kay] = average

    if average < 4.5:
        average_grade.popitem()


sorted_grade = dict(sorted(average_grade.items(),
                           key=lambda x: -x[1]
))

for i, k in sorted_grade.items():
    print(f'{i} -> {k:.2f}')