'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
'''

out_f = open('Output_task1.txt', 'w')

st = input('Insert info line by line. To stop, print empty line\n')

while not(st == ''):
    st += '\n'
    out_f.write(st)
    st = input()

out_f.close()
