#Home Work 5

#Task 1 imitation cash register

product_list = ['Новогодний Ежик', 'Кола', 'Мандарины', 'Помидоры']
product_price = [12, 50, 55, 30]
counter = 0
counter_finish = 0

z_report = []
buyer_list = []
buyer_list_amount = []

while counter < 1:
    print('Выберите позицию:')
    while counter < len(product_list):
        print(counter + 1, '. ', product_list[counter], ' : ', product_price[counter], sep='')
        counter += 1
    print(len(product_list) + 1, '. ', '(Завершить покупку)', sep='')
    print(len(product_list) + 2, '. ', '(Закрыть смену)', sep='')
    product_input = int(input('Выберите товар по номеру из списка: '))
    counter = 0
    if 1 <= product_input <= len(product_list):
        product_amount = int(input('Введите колличество: '))
        buyer_list.append(product_input)
        buyer_list_amount.append(product_amount)
    elif product_input == len(product_list) + 1:
        total_amount = []
        for product in buyer_list:
            print(counter+1, '. ', product_list[product-1], ' : ', product_price[product-1], ' * ',
                  buyer_list_amount[counter], ' = ', int(product_price[product-1] * buyer_list_amount[counter] * 1.12),
                  ' c НДС 12 %', sep='')
            total_amount.append(product_price[product-1] * buyer_list_amount[counter])
            counter += 1
        print('Итого:', int(sum(total_amount) * 1.12), 'c НДС 12%')
        z_report.append(sum(total_amount))
        counter = 0
        continue
    elif product_input == len(product_list) + 2:
        print('Выручка за смену:', int(sum(z_report) * 1.12), 'с НДС 12 %')
        counter += 1
    else:
        print('Вы ввели не верно значение, повторите ввод')

#Task 2 Prime Number Program

# data = int(input())
# list_of_primes = []
# counter = 0
#
# for desired_prime_number in range(1, data + 1):
#     for number_to_divide in range(1, desired_prime_number + 1):
#         if desired_prime_number % number_to_divide == 0:
#             counter += 1
#     if counter == 2:
#         list_of_primes.append(desired_prime_number)
#         print(desired_prime_number)
#     counter = 0
#
# print(list_of_primes)


a = 123
#Привет Андрей