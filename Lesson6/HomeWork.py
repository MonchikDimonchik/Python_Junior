# 6.1
# 1) Ввести с клавиатуры число n
# 2) Ввести с клавиатуры число m
# 3) Сформировать двумерный массив NxM из вводимых пользователем чисел
# 4) Распечатать получившийся массив
#
# Пример ввода:
# 2  # m
# 2  # n
# 1
# 2
# 3
# 4
#
# Пример вывода:
# [1, 2]
# [3, 4]
#
# 6.2
# 1) Первые 4 задания из предыдущего задания.
# 2) Поменять местами строки, содержащие наибольший элемент и наименьший элемент.
# P.S. Предполагается что таких элементов не больше одного.
#
# Пример ввода:
# 2  # m
# 2  # n
# 1
# 2
# 3
# 4
#
# Пример вывода:
# [1, 2]
# [3, 4]
#
# [3, 4]
# [1, 2]
#
# 6.3
# 1) Первые 4 задания из предыдущего задания.
# 2) Поменять местами строки и столбцы
# Пример ввода:
# 2  # m
# 2  # n
# 1
# 2
# 3
# 4
#
# Пример вывода:
# [1, 2]
# [3, 4]
#
# [4, 3]
# [2, 1]

#Task1

# n = int(input('Ввести с клавиатуры число n: '))
# m = int(input('Ввести с клавиатуры число m: '))
# matrix = []
#
# for item in range(n):
#     matrix.append([])
#     for values in range(m):
#         matrix[item].append(int(input()))
#
# for i in matrix:
#     print(i)

#Task2
n = int(input('Ввести с клавиатуры число n: '))
m = int(input('Ввести с клавиатуры число m: '))
matrix = []
max_number = 0
max_number_position_n = 0
max_number_position_m = 0
for item in range(n):
    matrix.append([])
    for values in range(m):
        matrix[item].append(int(input()))
        if matrix[item][values] > max_number:
            max_number_position_n = item
            max_number_position_m = values
            max_number = matrix[item][values]

min_number = max_number
min_number_position_n = 0
min_number_position_m = 0

for item in range(n):
    for values in range(m):
        if matrix[item][values] < min_number:
            min_number = matrix[item][values]
            min_number_position_n = item
            min_number_position_m = values

matrix[min_number_position_n], matrix[max_number_position_n] = matrix[max_number_position_n], matrix[min_number_position_n]

for i in matrix:
    print(i)

#Task3
