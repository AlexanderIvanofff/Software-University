import sys

fist_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_of_three_numbers(f, s, t):
    smallest_number = sys.maxsize
    if f < smallest_number:
        smallest_number = f
    if s < smallest_number:
        smallest_number = s
    if t < smallest_number:
        smallest_number = t
    return smallest_number


print(smallest_of_three_numbers(fist_number, second_number, third_number))