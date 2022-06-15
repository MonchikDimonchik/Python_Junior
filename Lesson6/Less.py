# user_input = int(input())
# count = 1
# count_two = user_input - 1
# # while count != user_input + 1:
# #     print('*' * count)
# #     count += 1
#
# # for i in range(1, user_input + 1):
# #     print('*' * i)
#
# #    *
# #   ***
# #  *****
# # *******
#
#
# while count < user_input + 1:
#     if count == 1:
#         print(' ' * (count_two + 1), '*')
#     print(' ' * count_two, '*' * (count * 2) + '*')
#     count += 1
#     count_two -= 1

# a = []
# count = 0
# for i in range(int(input())):
#     b = int(input())
#     if b > 0:
#         a.append(b * 3)
#     else:
#         a.append(b)
#     if b < 0:
#         count += 1
# print('Колличество отрицательых чисел', count)
# print(a)

#Task 1
# matrix = [
#     [1, 2, 3, 4],
#     [-1, 9, 0, -2],
#     [4, -2, 7, 1],
#     [4, 2, 2, -9]
# ]

# counter_first = 0
# counter_secon = 0
# for i in matrix:
#     counter_negativ_nubmer = 0
#     counter_secon = 0
#     for a in i:
#         if matrix[counter_secon][counter_first] < 0:
#             counter_negativ_nubmer += 1
#         counter_secon += 1
#     counter_first += 1
#     print('Количество отрицательых чисел в ', counter_first, '1-ом:', counter_negativ_nubmer)

#Task 2
user_input = int(input())
user_list = []

for i in range(user_input):
    user_list.append(int(input()))

counter = 0
min_ = user_list[0]
min_indx = 0
max_ = user_list[0]
max_indx = 0
for i in user_list:
    if i < min_:
        min_ = i
        min_indx = counter
    elif i > max_:
        max_ = i
        max_indx = counter
    counter += 1




print(min_, min_indx)