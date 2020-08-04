def solve(word, string):
    while word in string:
        string = string.replace(word, '')
    return string


first_str = input()
second_string = input()
print(solve(first_str, second_string))