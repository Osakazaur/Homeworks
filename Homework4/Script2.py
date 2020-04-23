'''
бесконечный итератор, генерирующий целые числа, начиная с указанного
использовать функцию count() и cycle() модуля itertools
'''

from itertools import count
from time import sleep

def generator(first : int):
    for el in count(first):
        print(el)
        sleep(0.5)
