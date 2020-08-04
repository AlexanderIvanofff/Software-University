def all_digit(text):
    all_char = ''
    for char in text:
        if char.isdigit():
            all_char += char
    return all_char


def letter(text):
    all_letter = ''
    for cher in text:
        if cher.isalpha():
            all_letter += cher

    return all_letter


def all_other_characters(text):
    other_characters = ''
    for char in text:
        if not char.isdigit() and not char.isalpha():
            other_characters += char
    return other_characters


current_text = input()

print(all_digit(current_text))
print(letter(current_text))
print(all_other_characters(current_text))