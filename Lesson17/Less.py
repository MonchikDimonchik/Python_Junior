class Human:
    def __init__(self, name, year, weight):
        self.name = name
        self.yaer = year
        self.weight = weight

    def hello(self, person):
        return f'Hello, {person.name}! My name is {self.name}'

dima = Human('Dima', 24, 100)
anton = Human('Anton', 29, 100)
print(dima.hello(anton))
print(anton.hello(dima))
# human = Human('Dima', 1995, 55)
# hello = human.hello('Anton')
# print(hello)


