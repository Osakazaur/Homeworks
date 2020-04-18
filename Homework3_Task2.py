"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def informaton(first_name,
               last_name,
               year_of_birth,
               city,
               email,
               phone_num ):
    print('{0} {1} was born in {2}, lives in {3}. You can contact him by e-mail {4} or phone number {5}.'.
          format(first_name, last_name, year_of_birth, city, email, phone_num))

informaton(*input('Print separated by space: first name, last name, year of birth, city, e-mail and phone number\n').
           split())
