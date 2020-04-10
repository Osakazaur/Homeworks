var_rev = input("Type the revenue:\n")
while True:
    if var_rev.isdigit():
        break
    else:
        var_rev = input("Type revenue:\n")
var_rev = int(var_rev)

var_cost = input("Type the costs:\n")
while True:
    if var_cost.isdigit():
        break
    else:
        var_cost = input("Type the costs:\n")
var_cost = int(var_cost)

var_res = var_rev - var_cost

if var_res > 0:
    print("Your firm is profitable")
    var_rent = var_res / var_rev
    print("The profitable of your firm is %.2f" % var_rent)

    var_emp = input("Type the number of your employers:\n")
    while True:
        if var_emp.isdigit():
            break
        else:
            var_emp = input("Type the number of your employers:\n")
    var_emp = int(var_emp)
    var_res_per_emp = var_res / var_emp
    print("The profit per enmployer is %.2f" % var_res_per_emp)
else:
    print("Your firm is unprofitable")
