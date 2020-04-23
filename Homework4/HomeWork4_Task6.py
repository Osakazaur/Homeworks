'''
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from Script2 import generator
from Script3 import repeater

cmd = input('Generator module: print G\nRepeater module: print R\n')
if cmd == 'G':
    generator(int(input('Type the first number\n')))
elif cmd == 'R':
        repeater(input('Type list elements separated by space\n').split())
