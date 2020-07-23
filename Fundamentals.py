n = int(input())
word = input()

search_word = []
all_text = []
for i in range(n):
    text = input()
    all_text.append(text)

    if word in text:
        search_word.append(text)

print(all_text)
print(search_word)
