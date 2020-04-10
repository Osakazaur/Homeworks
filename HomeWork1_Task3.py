n = input("Type number:\n")
while True:
    if n.isdigit():
        break
    else:
        n = input("Type number:\n")

n = int(n)
n = n + (n*10 + n) + (n*100 + n*10 + n)
print("The answer is %d" % n)
