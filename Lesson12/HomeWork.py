# HOMEWORK 12

# TASK 1

# def my_map(function, data):
#     counter = 0
#     for element_list in data:
#         data[counter] = function(element_list)
#         counter += 1
#     return data


# TASK 2

# def my_filter(function, data):
#     counter = 0
#     for element_list in data:
#         if function(element_list):
#             counter += 1
#             continue
#         else:
#             data.remove(data[counter])
#             counter += 1
#     return data
#
#
# def is_even(x):
#     return x % 2 == 0
#
#
# result = my_filter(is_even, [1, 2, 3, 4, 5, 6])
#
# print(result)  # [2, 4, 6]

# TASK 3

# def my_zip(first, second):
#     counter = 0
#     list_tuples = []
#     minimum_number = len(first) - len(second)
#     if minimum_number < 0:
#         for i in first:
#             list_tuples.append((first[counter], second[counter]))
#             counter += 1
#     else:
#         for i in second:
#             list_tuples.append((first[counter], second[counter]))
#             counter += 1
#     return list_tuples
#
# result = my_zip([1, 3, 5, 7], [2, 4, 6])
# print(result)  # [(1, 2), (3, 4), (5, 6)]
#
# # Ещё пример:
#
# result = my_zip([1], [2, 4, 6])
# print(result)  # [(1, 2)]