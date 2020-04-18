""""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
"""

def sum_func(*args):
    global res
    try:
        for el in args:
            res += int(el)
        return res
    except ValueError:
            print('There are wrong symbols')

res = 0

while True:
    input_list = (input("Type numbers separated by space.\nTo stop type 'N'\n").split())

    if input_list[-1] == 'N':
        print(sum_func(*input_list[:len(input_list)-1]))
        break
    else:
        print(sum_func(*input_list))
