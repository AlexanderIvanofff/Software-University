cards = input().split(' ')
faro_shuffles = int(input())
length_faro = len(cards) // 2
res = 0

for i in range(faro_shuffles):
    res = []

    for index in range(length_faro):
        first_cards = cards[index]
        current_index_second_cards = index + length_faro
        second_cards = cards[current_index_second_cards]

        res.append(first_cards)
        res.append(second_cards)

    cards = res

print(res)