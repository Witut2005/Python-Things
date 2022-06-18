
def divide(number, divisor):
    if number == 0:
        return 0

    elif number < 0:
        return -1

    else:
        return 1 + divide(number - divisor, divisor)


var1 = input("type non-negative number: ")
var2 = input("type non-negative number: ")

var1 = int(var1)
var2 = int(var2)

var1 = abs(var1)
var2 = abs(var2)

print("result: ", divide(var1, var2))