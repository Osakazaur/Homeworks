n = input("Type number:\n")
while True:
    if n.isdigit():
        break
    else:
        n = input("Type number:\n")
n = int(n)

max = 0
while n > 0:
    a = n % 10
    if a > max:
        max = a
    n = n // 10

print("The answer is %d" % max)
