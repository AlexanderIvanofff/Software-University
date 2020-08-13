text = input()

occurrences = {}

for ch in text:
    if ch == ' ':
        continue

    if ch in occurrences:
        occurrences[ch] += 1
    else:
        occurrences[ch] = 1

for kay, values in occurrences.items():
    print(f'{kay} -> {values}')