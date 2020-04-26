'''
4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

dict_replace = dict(
                    One='Один',
                    Two='Два',
                    Three='Три',
                    Four='Четыре'
                    )

out_f = open('Output_task4.txt', 'w')

try:
    with open("Input_task4.txt") as in_f:
        for line in in_f:
            data_list = line.split(' - ')
            data_list[0] = dict_replace.get(data_list[0])
            print(data_list)
            out_f.write('{} - {}'.format(data_list[0], data_list[1]))
except IOError:
    print('File not found')