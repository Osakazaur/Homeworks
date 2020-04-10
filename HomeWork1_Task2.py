time = input("Type number of seconds:\n")

while True:
    if time.isdigit():
        break
    else:
        time = input("Type number of seconds:\n")
# Сообщение для преподавателя:
# мне кажется, этот код можно сделать короче, без повторений, но не знаю как.

time = int(time)
seconds = time % 60
time = time // 60
minutes = time % 60
time = time // 60
hours = time % 24

print("{0:>02}:{1:>02}:{2:>02}".format(hours, minutes, seconds))
