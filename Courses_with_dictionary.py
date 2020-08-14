from collections import defaultdict

data = defaultdict(list)

while True:
    command = input()
    if command == 'end':
        break

    program_name, user_names = command.split(" : ")

    data[program_name] += [user_names]

sorted_dict = dict(sorted(data.items(), key=lambda name: -len(name[1])))

for kay, values in sorted_dict.items():
    print(f'{kay}: {len(values)}')

    for user_names in sorted(values):
        print(f'-- {user_names}')