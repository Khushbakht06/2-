# Лабораторная №2. Регулярные выражения
#   Вариант 10.
# Натуральные числа. Выводит на экран нечетные числа, меняя порядок цифр в них на обратный. Полиндромы (значения не меняется от смены цифр) - выводятся прописью.

import re

def is_palindrome(num_str):
    return num_str == num_str[::-1]

def number_to_words(num_str):
    num_words = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(num_words[digit] for digit in num_str)

def process_number(num_str):
    if is_palindrome(num_str):
        return number_to_words(num_str)
    else:
        return num_str[::-1]

def is_odd(num_str):
    return int(num_str) % 2 != 0

def process_lexeme(lexeme):
    if re.match(r'^\d+$', lexeme):  # Check if lexeme is a natural number
        if is_odd(lexeme):
            return process_number(lexeme)
    return lexeme  # Return the original lexeme if it's not a natural number

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lexemes = re.findall(r'\b\d+\b|\b\w+\b', content)
        for lexeme in lexemes:
            print(process_lexeme(lexeme), end=' ')

# Example usage:
file_path = r'C:/student\2 сем\2lab.py/input.txt'
process_file(file_path)

