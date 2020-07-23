def get_characters(start, end):
    res = []
    for i in range(ord(start)+1, ord(end)):
        res.append(chr(i))
    return res


a = input()
b = input()
result = get_characters(a, b)
print(' '.join(result))