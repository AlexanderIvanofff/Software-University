def int_str(string_number, count_number_to_remove):
    numbers = []

    for num in string_number:
        numbers.append(int(num))

    for i in range(count_number_to_remove):
        numbers.remove(min(numbers))
    return numbers


str_num = input().split(' ')
count_num_to_remove = int(input())
print(int_str(str_num, count_num_to_remove))