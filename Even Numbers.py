numbers = list(map(lambda x: int(x), input().split(',')))
even_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(i)

print(even_numbers)