def reverse(text):
    return text[::-1]


res ={}
while True:
    command = input()
    if command == 'end':
        break
    res[command] = reverse(command)


for kay, value in res.items():
    print(f'{kay} = {value}')