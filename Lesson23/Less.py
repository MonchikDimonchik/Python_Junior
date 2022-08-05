# class Person:
#     pass
#
#
# instance = []
# print(bool(instance))
#
#
# def get_person():
#     print(bool(instance))
#     if instance:
#         pass
#     else:
#         instance.append(1)
#         return Person()
#
#
# person1 = get_person()
# person2 = get_person()
#
# print(bool(instance))
# print(isinstance(person1, Person))
# print(person1 is person2)



class Person:
    instance = None
    def get_object():
