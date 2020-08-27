def reverse(text):
    stack = []
    for ch in text:
        stack.append(ch)

    reverse_str = []
    while stack:
        ch = stack.pop()
        reverse_str.append(ch)

    return reverse_str


string = input()
print(''.join(reverse(string)))