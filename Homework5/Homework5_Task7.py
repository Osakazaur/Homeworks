'''
7.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''

from json import dump

firm_dict = {}
av_list = [0, 0]

try:
    with open("Input_task7.txt", encoding='utf-8') as in_f:
        for line in in_f:
            firm_list = line.split()
            firm_key = firm_list[0]
            firm_prof = int(firm_list[2]) - int(firm_list[3])

            firm_dict.setdefault(firm_key)
            firm_dict[firm_key] = firm_prof

            if firm_prof > 0:
                av_list[0] += firm_prof
                av_list[1] += 1

    firm_list = [firm_dict, dict(average_profit=av_list[0] / av_list[1])]
    print(firm_list)

except IOError:
    print('File not found')

with open("Output_task7.json", "w") as out_f:
    dump(firm_list, out_f)
