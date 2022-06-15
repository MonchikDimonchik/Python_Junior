# def bar(y):
#     return y ** 3
#
# print(bar(5))

a = 1
b = 2
c = 3
d = 4
# def my_max4(a, b, c, d):
#     return my_max(my_max(my_max(a, b), c), d)

# print(my_max4(a, b, c, d))


numbers = [6, 3, 8, 2, 8, 3, 5, 9, 12, 33, 2, 3, 7, 5, 9]
max_number = 0


def my_max(a, b):
    if a > b:
        return a
    return b

def my_max_n(my_max):
    max_number = 0
    for number in numbers:
        if number < my_max(number, max_number):
            max_number = number


print(my_max_n(numbers))
