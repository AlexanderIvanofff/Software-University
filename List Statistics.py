n = int(input())

even_number = []
odd_number = []
for i in range(n):
    number = int(input())
    if number < 0:
        odd_number.append(number)
    elif number >= 0:
        even_number.append(number)

print(even_number)
print(odd_number)
print(f'Count of positives: {len(even_number)}. Sum of negatives: {sum(odd_number)}')