import time

a = time.time()


def bar(n):
    print('Вывод')
    time.sleep(3)
    print('Прошло 3 секунды')
    return n

print(a)
print(time.time() - bar(time.time()))