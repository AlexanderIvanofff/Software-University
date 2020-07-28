n = int(input())
search_word = input()

list_str = []
filtered_word = []
for i in range(n):
    current_str = input()
    list_str.append(current_str)
    if search_word in current_str:
        filtered_word.append(current_str)


print(list_str)
print(filtered_word)