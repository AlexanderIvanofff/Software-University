n = int(input())
command = input()
# Четем всякакви числа с различен брой цифри до получаване на команда STOP
# за всяко число намираме сумата от цифрите му и дали е специално спрямо условието от задача 6

is_special = True
while command != "STOP":
    number = int(command)
    saved_number = number
    while number > 0:
        # 1. вземем стойността на последната цифра -> проверка
        last_digit = number % 10
        if n % last_digit != 0:
            is_special = False
            break
        # 2. махнем последната цифра от числото
        number //= 10
    if is_special:
        print(f'Number {saved_number} is special')
    else:
        print(f'Number {saved_number} is not special')
    command = input()