'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.
'''

try:
    with open("Input_task3.txt") as in_f:
        print('Employers with salary less than 20k:')
        sal_sum = 0
        emp = 0
        for line in in_f:
            emp_list = line.split()
            if int(emp_list[1]) < 20:
                print(emp_list[0])
            sal_sum += int(emp_list[1])
            emp += 1
        print('\nAverage salary: {:.2f}'.format(sal_sum/emp))
except IOError:
    print('File not found')

