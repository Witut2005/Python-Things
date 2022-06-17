

def if_parity(x):
    return not x & 1

var = input("type number: ")
print("is parity: ", if_parity(int(var)))