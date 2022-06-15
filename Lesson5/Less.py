# data = [
#     '1', 2, 3.0, True, None, []
# ]
#
# # Линейная структура данных
# # Все элементы списка проиндексированы
#
# a = data[3]
#
# print(a)
#
# print(list('asdfghjkl'))
#
# # [] - False
# print(bool([]))
#
# # append - добавить элемент в список
# data.append(4)
# print(data)
#
# data.insert(0, 123)
#
# print(data)
#
# data.insert(4, 5)
# print(data)
#
# data.pop(2)
# print(data)
#
# data.remove(None)
# print(data)
#
# data = ['1', 2, 3.0, True, None, [], 4]
#
#
# a = range(10)
# print(list(a))
#
# for i in range(1, 11):
#     print(i)


# data = [123, '1', 2, 3.0, 5, True, None, [], 4]
# data_len = len(data)
# counter = 0
# while counter != data_len:
#     print(data[counter])
#     counter += 1
#
# for i in range(len(data)):
#     print(data[i])
#
# for i in data:
#     print(i)
#


# user_input = int(input())
# range_user = range(user_input)
#
# date = []


# for item in range_user:
#     user_input = int(input())
#     if user_input % 2 > 0:
#         date.append(user_input)

# for i in date:
#     print(i * 2)
# Prime Number Program

data = int(input())
list_of_primes = []
counter = 0

for desired_prime_number in range(1, data + 1):
    for number_to_divide in range(1, desired_prime_number + 1):
        if desired_prime_number % number_to_divide == 0:
            counter += 1
    if counter == 2:
        list_of_primes.append(desired_prime_number)
        print(desired_prime_number)
    counter = 0

print(list_of_primes)