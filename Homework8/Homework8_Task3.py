'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
'''

my_list = []
print('Insert items line by line. To stop, print STOP')
while 1:
    inp = input()
    if inp == 'STOP':
        break
    else:
        try:
            my_list.append(int(inp))
        except ValueError:
            print('Items might be only numbers')

print(my_list)
