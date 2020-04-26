'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран
'''

subj_dict = {}

try:
    with open("Input_task6.txt", encoding='utf-8') as in_f:
        for line in in_f:
            subj_list = line.split()
            subj_key = subj_list[0]
            subj_list.pop(0)

            subj_sum = 0
            for el in subj_list:
                if el == '-':
                    x = 0
                else:
                    x = ''
                    x = x.join(i for i in el if i.isdigit())
                subj_sum += int(x)

            subj_dict.setdefault(subj_key)
            subj_dict[subj_key] = subj_sum

        print(subj_dict)

except IOError:
    print('File not found')