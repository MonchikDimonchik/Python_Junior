# Home Work 4

# Task 1
# date_ = []
# count = 0
# count_error = 0
# while count < 10:
#     a = int(input('Введите число в диапазоне от 0 до 10: '))
#     count += 1
#     if 0 > a or a > 10:
#         while count_error < 3:
#             if 0 > a or a > 10:
#                 count_error += 1
#                 a = int(input('Ошибка, введите число в диапазоне от 0 до 10: '))
#             else:
#                 date_.append(a)
#                 count_error = 0
#                 break
#     else:
#         date_.append(a)
#
# sum_positive = 0
# number_positive = []
# average = 0
#
# for item in date_:
#     if item > 0:
#         number_positive.append(item)
#     sum_positive += item
# print(sum(number_positive))
# print(round(sum_positive / len(date_), 2))

# Task 2
# import random
#
# secret_number = random.randint(1, 10)
# attempt_counter = 0
#
# while True:
#     user_input = int(input('Угадайте загаданное число: '))
#     attempt_counter += 1
#     if user_input < 0 or user_input > 10:
#         print('Введите число в диапазоне от 0 до 10')
#         continue
#     else:
#         if user_input < secret_number:
#             print('Загаданное число больше')
#         elif user_input > secret_number:
#             print('Загаданное число меньше')
#         else:
#             print('Вы угадали ! Число ', secret_number, '\n', 'Колличество попыток ', attempt_counter, sep='')
#             break
