"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""

def my_func(a, b, c : int):
    '''
    returns sum of 2 maximum elements

    :param a: first element
    :param b: second element
    :param c: third element
    :return: sum of 2 maximum elements
    '''
    if (a>c) and (b>c):
        max1 = a
        max2 = b
    elif (a>b) and (c>b):
        max1 = a
        max2 = c
    elif (b>a) and (c>a):
        max1 = b
        max2 = c

    return max1 + max2

print(my_func(*map(int, input('Type 3 arguments separated by space\n').split())))