'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
элемента.
'''

from random import randint

my_list = [randint(0, 11) for _ in range(10)]
print(my_list)

new_list = [el for i, el in enumerate(my_list) if (i > 1) and (el > my_list[i-1])]
print(new_list)
