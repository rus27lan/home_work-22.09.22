# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# from curses.ascii import isdigit


# number = input()
# sum = 0
# for i in number:
#     if i.isdigit():
#         sum += int(i)
# print(sum)


# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# number = int(input("Введите число N "))
# numbers = []
# count = 1
# number2 = 1
# while count - 1 < number:
#     number2 *= count
#     numbers.append(number2)
#     count += 1
# print(numbers)


# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

# number = int(input("Введите число N "))
# numbers = []
# count = 1
# number2 = 1
# sum = 0
# while count - 1 < number:
#     number2 = (1 + 1/number) ** number
#     numbers.append(number2)
#     count += 1
#     sum += number2
# print(sum)


# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

import random
number = int(input("Введите число N "))
numbers = []
number2 = - (number)
while number2 < number + 1:
    numbers.append(number2)
    number2 += 1
print(numbers)
count = 0
result = 1
while count < number:
    my_file = open("file.txt", "a+")
    text = random.randrange(number)
    my_file.write(f"{str(text)}\n ")
    count += 1
    result = numbers[text] * result

my_file = open("file.txt", "a+")
my_file.write(str(result))
my_file.close()




# 18). Реализуйте алгоритм перемешивания списка.

# import random


# list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(f"оригинал: {list}")
# random.shuffle(list)
# print(f"перемешиванный: {list}")

# -------------------------------------------------------------------------------------------
# Задания лекции
# import random


# num = int(input("Введите число N "))
# num_N = 0
# numbers = []
# while num_N < num:
#     number = random.randrange(-100, 100)
#     if num_N < num:
#         numbers.append(number)
#     num_N = num_N + 1
# print(numbers)

# num = int(input("Введите число N "))
# numbers = []
# number = 1
# number2 = 1
# while number - 1 < num:
#     number2 = 3 * number + 1
#     numbers.append(number2)
#     number = number + 1
# print(numbers)


# n = 0
# while n < 2:
#     text1 = input()
#     text2 = input()
#     n = 2
# print(text1, text2)
