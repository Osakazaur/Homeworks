# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и через dict.

mounth = input('Type the mounth\n')

list_winter = ['January', 'February', 'December']
list_spring = ['March', 'April', 'May']
list_summer = ['June', 'July', 'August']
list_fall = ['September', 'October', 'November']

if mounth in list_winter:
    print('Winter')
elif mounth in list_spring:
    print('Spring')
elif mounth in list_summer:
    print('Summer')
elif mounth in list_fall:
    print('Fall')

seasons_dict = dict(January = 'Winter', February = 'Winter',
                    March = 'Spring', April = 'Spring',
                    May = 'Spring', June = 'Summer',
                    July = 'Summer', August = 'Summer',
                    September = 'Fall', October = 'Fall',
                    November = 'Fall', December = 'Winter')

print(seasons_dict.get(mounth))
