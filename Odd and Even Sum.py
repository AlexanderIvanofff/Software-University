def odd(numbers):
    even = 0
    number_str = str(numbers)

    for index, digit in enumerate(number_str):
        if int(digit) % 2 == 0:
            even += int(digit)

    return even


def even(numbers):
    odd = 0
    number_str = str(numbers)

    for index, digit in enumerate(number_str):
        if int(digit) % 2 != 0:
            odd += int(digit)

    return odd


number = int(input())
even_sum = even(number)
odd_sum = odd(number)

print(f'Odd sum = {even_sum}, Even sum = {odd_sum}')