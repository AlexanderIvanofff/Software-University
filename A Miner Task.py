from collections import defaultdict

type_of_metal = input()

total_count = defaultdict(int)
while type_of_metal != 'stop':
    quantity = int(input())

    total_count[type_of_metal] += quantity

    type_of_metal = input()


for kay, values in total_count.items():
    print(f'{kay} -> {values}')