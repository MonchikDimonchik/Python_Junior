import time

a = time.time()


def bar(n):
    print('Вывод')
    time.sleep(3)
    print('Прошло 3 секунды')
    return n

print(a)
print(time.time() - bar(time.time()))


def timer(function):
    def wrapper(n):
        start_time = time.time()
        result = function(n)
        print(time.time() - start_time)
        return result
    return wrapper


@timer
def bar(n):
    time.sleep(n/2)


@timer
def sqr(a):
    return a ** 2

@timer
def test_dekorator(argument):
    print('Ой че щас будет')
    return argument()


print(test_dekorator(timer))