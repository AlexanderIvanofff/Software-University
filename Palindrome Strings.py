strings = input().split(' ')
searched_palindromes = input()

palindromes = [word for word in strings if word == word[::-1]]
palindromes_count = palindromes.count(searched_palindromes)



print(palindromes)
print(f'Found palindrome {palindromes_count} times')