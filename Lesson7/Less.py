#Task 1
# user_input = int(input())
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# matrix_2 = [[], [], []]
# count = 0
# count_2 = 0
#
#
# for i in matrix:
#     for a in i:
#         matrix_2[count].append(a * user_input)
#         count_2 += 1
#     print(matrix_2[count])
#     count += 1

#Task 2
# user_input = int(input())
# user_list = []
#
# for i in range(user_input):
#     user_list.append(int(input()))
#
# counter = 0
# min_ = user_list[0]
# min_indx = 0
# max_ = user_list[0]
# max_indx = 0
# for i in user_list:
#     if i < min_:
#         min_ = i
#         min_indx = counter
#     elif i > max_:
#         max_ = i
#         max_indx = counter
#     counter += 1
#
# user_list[min_indx], user_list[max_indx] = user_list[max_indx], user_list[min_indx]
#
# print(user_list)
# print(min_, min_indx)

#Task 3
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
counter_horizontal = 0
counter_vertical = 0
D_indx = 0
D = []
len_vertical_matrix = len(matrix)
len_horizontal_matrix = len(matrix[0])
print(len_vertical_matrix)
for i in matrix:
    for a in i:
        if counter_horizontal >= len_vertical_matrix:
            counter_horizontal = 0
        D_indx += matrix[counter_horizontal][counter_vertical]
        counter_horizontal += 1
    counter_vertical += 1
    counter_horizontal = 0
    D.append(D_indx)
    D_indx = 0
print(D)
# Вычислить вектор D, который состоит из сумм элементов каждой строки
# Вывести вектор D на экран:
# прим: [8, 12, 20]






# for i in matrix:
#     for a in i:
#         matrix[count][count_2] = matrix[count][count_2] * user_input
#         if count_2 == 2:
#             print(matrix[count][count_2])
#         else:
#             print(matrix[count][count_2], end=' ')
#         count_2 += 1
#     count_2 = 0
#     count += 1