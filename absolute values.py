def absolute_values(numbers):
    return [abs(x) for x in numbers]


print(absolute_values(map(float, input().split(' '))))