def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def is_negative(number):
    return number < 0


def is_positive(number):
    return number >= 0


FILTERS_MAP = {
    'even': is_even,
    'odd': is_odd,
    'negative': is_negative,
    'positive': is_positive,
}

n = int(input())

number = [int(input()) for i in range(n)]
command = input()

filter_fn = FILTERS_MAP[command]
print([n for n in number if filter_fn(n)])