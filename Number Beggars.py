string = input().split(', ')
number_beggars = int(input())
numbers = []

for number_of_beggars in string:
    numbers.append(int(number_of_beggars))

beggars = []
for i in range(number_beggars):
    beggars.append(0)

index = 0
for number in numbers:
    beggars[index] += number
    index += 1

    if index == number_beggars:
        index = 0

print(beggars)