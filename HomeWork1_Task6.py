a_dist = input("Insert first distance:\n")
while True:
    if a_dist.isdigit():
        break
    else:
        a_dist = input("Insert first distance:\n")
a_dist = int(a_dist)

b_dist = input("Insert required distance:\n")
while True:
    if b_dist.isdigit():
        break
    else:
        b_dist = input("Insert required distance:\n")
b_dist = int(b_dist)

# Сообщение преподавателю
# Тут я хотела сделать проверку, что введённое a меньше b и при невыполнении запросить переввести данные,
# но код получается костыльно-громоздкий

i = 1
while a_dist < b_dist:
    a_dist *= 1.1
    i += 1
print("Distance reached on %d day" % i)
