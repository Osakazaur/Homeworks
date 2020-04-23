'''
бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее
 использовать функцию count() и cycle() модуля itertools
'''

from itertools import cycle
from time import sleep

def repeater(base_list : list):
    for el in cycle(base_list):
        print(el)
        sleep(0.5)