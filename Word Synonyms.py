from collections import defaultdict

synonyms = defaultdict(list)

n = int(input())

for _ in range(n):
    word = input()
    synonym = input()
    synonyms[word].append(synonym)


for word, synonym in synonyms.items():
    normalized_synonyms = ', '.join(synonym)
    print(f'{word} - {normalized_synonyms}')