'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

def exponentiation1(x: float, y : int):
    '''
    Exponentitation func for bult-in function

    :param x: base -> float
    :param y: power -> int
    :return: x power y -> float
    '''
    if y < 0:
        return 1/(x**(-1*y))
    else:
        print('Exponent required negative\n')
        a, b = input('Type 2 arguments separated by space\n').split()
        print(exponentiation1(float(a), int(b)))

def exponentiation2(x: float, y : int):
    try:
        if y < 0:
            i = 0
            while i < -1*y:
                res = x*x
                i += 1
            return 1/res
    except ZeroDivisionError:
        print('Division by zero!')
    else:
        print('Exponent required negative\n')
        a, b = input('Type 2 arguments separated by space\n').split()
        print(exponentiation1(float(a), int(b)))

a, b = input('Type 2 arguments separated by space\n').split()
print(exponentiation1(float(a), int(b)))
print(exponentiation2(float(a), int(b)))