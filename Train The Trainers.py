count_jury = int(input())
total_grade = 0
total_average_score = 0
total_presentation = 0

line = input()
while line != 'Finish':
    presentation = line
    total_presentation += 1
    for i in range(1, count_jury + 1):
        score = float(input())
        total_grade += score
    average_grade = total_grade / count_jury
    total_average_score += average_grade

    print(f'{presentation} - {average_grade:.2f}.')
    total_grade = 0
    line = input()
avg_total_presentation = total_average_score / total_presentation
print(f"Student's final assessment is {avg_total_presentation:.2f}.")