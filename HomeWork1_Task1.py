# Сообщение для преподавателя:
# здесь сделано больше, чем просилось в задании: мне хотелось испробовать новые приёмы из урока.

var_hw = "Hello, World!"
print(var_hw)

var_days = 1;
print("This is my {0} day studying Python!".format(var_days))

your_name = input("Let's know each other more!\nWhat's your name?\n")
print("Nice to meet ya, %s!" % your_name)

your_year = input("In what year you were born?\n")
while True:
    if your_year.isdigit():
        break
    else:
        your_year = input("Please, type a number!\n")

have_bitrh = input("Have you had celebrated your birthday in this year yet? Please, type 'Y' or 'N'\n")

while True:
    if have_bitrh == 'Y':
        age = 2020 - int(your_year)
        break
    elif have_bitrh == 'N':
        age = 2019 - int(your_year)
        break
    else:
        have_bitrh = input("I don't understand. Please, type 'Y' or 'N'\n")

print("Your are %d years old, right?" % age)
