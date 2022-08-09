class Field:
    def __init__(self):
        self.field = []

        for line_x in range(10):
            self.field.append([])
            for line_y in range(10):
                self.field[line_x].append('.')

    def show(self):
        letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        count = 0
        field_str = ' '

        for latter in letter_list:
            field_str += latter + ' '
            count += 1
        count = 0
        field_str += '\n'

        for line_x in self.field:
            field_str += str(numbers_list[count])
            count += 1
            for line_y in line_x:
                field_str += line_y + ' '
            field_str += '\n'
        return field_str


Field1 = Field()
print(*Field1.show())
