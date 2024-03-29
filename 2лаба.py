# Лабораторная №2. Регулярные выражения
#   Вариант 10.
# Натуральные числа. Выводит на экран нечетные числа, меняя порядок цифр в них на обратный. Полиндромы (значения не меняется от смены цифр) - выводятся прописью.
import re
numbers = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}
# Функция для инвертирования числа
def invert_number(number):
    return int(str(number)[::-1])

# Функция для проверки на палиндром
def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Создаем файл example.txt и записываем в него данные
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('1234567890')

# Получаем цифру от пользователя
start_digit = input("Введите цифру (от 0 до 9), с которой должны начинаться нечетные числа: ")

# Считываем данные из файла и обрабатываем их
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Используем регулярные выражения для поиска чисел
        numbers_list = re.findall(r'\d+', line)
        
        for number_str in numbers_list:
            if number_str.startswith(start_digit):
                number = int(number_str)
                if number % 2 != 0:  # Проверка на нечетность
                    if is_palindrome(number):
                        print(number_str, end=' ')
                    else:
                        print(invert_number(number), end=' ')
                    print()  # Добавляем перевод строки после каждого числа
