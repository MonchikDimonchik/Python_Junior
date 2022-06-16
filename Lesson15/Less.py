def lm(a, b):
    return a + b


print(lm(5, 6))

print((lambda a, b: a + b)(1, 2))

print((lambda x: x % 2 == 0)(4))

a = (lambda x: x % 2 == 0)(4)

print(a)


def by_values(item):
    return item[1]


# print(sorted(d.item(), key=lambda item: item[1]))

def is_odd(x):
    return x % 2 == 1


print(is_odd(3))

unfiltered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = []
for i in unfiltered_list:
    if is_odd(i):
        a.append(i)
print(a)


print(list(filter((lambda x: x % 2), unfiltered_list)))

def square(x):
    return x ** 2

counter = 0
for i in unfiltered_list:
    unfiltered_list[counter] = square(i)
    counter += 1
print(unfiltered_list)

print(list(map(square, unfiltered_list)))
print(list(map(lambda x: x ** 2, unfiltered_list)))