'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint

with open('Output_task5.txt', 'r+') as out_f:
    # writing section
    for _ in range(10):
        out_f.write(str(randint(0, 10)))
        out_f.write(' ')

    # reading section
    out_f.seek(0)
    print(sum(map(int, out_f.read().split())))
