""""
 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
 пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def division(x, y : int):
    '''
    Function of division

    :param x: divident
    :param y: divider
    :return: private
    '''
    try:
        return x/y
    except ZeroDivisionError:
        print('Division by zero!')

print(division(*map(int, (input('Type 2 arguments separated by space\n').split()))))
