result = 5


# def foo(result):
#     return result * 2


# print(foo(result))

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Donec hendrerit arcu ac leo mollis sollicitudin. 
Morbi interdum neque tellus, in efficitur justo elementum id. 
Sed nec vestibulum nunc, vel pellentesque purus. 
Etiam a vehicula arcu. Proin vel leo dui. 
Sed convallis sollicitudin leo, eget tempus risus luctus ac. 
Proin urna nibh, hendrerit ut iaculis vel, pulvinar nec purus.
"""



def remove(text):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'Y', 'y', 'U', 'u', 'O', 'o']
    Changed_text = text
    for letter in vowels:
        Changed_text = Changed_text.replace(letter, '')
    print(Changed_text)
#     # text2 = []
#     # for letter in text:
#     #     text2.append(letter)
#     # text = ''
#     # for letter in text2:
#     #     if letter in vowels:
#     #         letter = ''
#     #     text += letter
#     # print(text)


remove(text)


teee = "How can mirrors be real if our eyes aren't real"
a = ''
for i in teee.split():
    a += i[0].upper() + i[1:] + ' '
print(a)

# def remove_vowels(text):
#     return text.replace('A', '', 'E', '')

text = "How can mirrors be real if our eyes aren't real"
text_2 = text.split()
list_ = []
for i in text_2:
    list_.append(i.capitalize())
print(list_)