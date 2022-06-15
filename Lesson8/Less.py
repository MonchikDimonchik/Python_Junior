# my_dict = {
#     'Ключ': 'Значение'
# }
#
#
# my_dict['hi'] = 'привет'
#
# print(my_dict)

# d = [7, 7, 2, 3, 6, 23]
# d.pop(4)
# d.insert(4, 5)
# print(d)

# my_dict = {
#     'Кукла': 12,
#     'Медведь': 32,
#     'Паровозик': 5,
#     'Нож': 6,
# }

# user_input = input()

# print(my_dict.get('hi'))
# print(123)


my_dict = {
    1: 'Вы ввели еденицу',
    2: 'абсолютно разные значения',
    3: 'некоторый текст',
    4: 'вы ввели 4'
}

while True:
    user_input = int(input())
    if user_input not in my_dict:
        print(my_dict.get(user_input, 'что то пошло не так'))
        continue
    else:
        print(my_dict[user_input])
        break
