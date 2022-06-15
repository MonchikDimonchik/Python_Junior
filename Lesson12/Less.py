# from builtins import function
# from builtins import function


def bar(a, b=[]):
    s = []
    s += b
    for i in range(a):
        s.append(i)
    return s


result = bar(5, [1, 2, 3])
print(result)
result = bar(5)
print(result)
result = bar(5)
print(result)


# def people():
#     print(1)
#
#
# s = {'p': people, }
# s['p']()
# k()
# if input_user in s.keys():
#     k = input_user()

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


def people():
    user_input1 = input('Введите, пожалуйста, номер документа:')
    for i in documents:
        if i['number'] == user_input1:
            print(i['name'])


moxito = {'p': people()}

moxito['p']