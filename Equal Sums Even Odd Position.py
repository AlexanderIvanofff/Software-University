firs_number = int(input())
second_number = int(input())

for number in range(firs_number, second_number + 1):
    number_str = str(number)

    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(number_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(f'{number}', end=' ')