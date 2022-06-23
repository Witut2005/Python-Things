

import math

func = lambda x: x + 10

var1 = input("type first number: ")

print("First round func ", round(float(var1), 2))
print("Second round func ", round(float(var1)))

tmp = divmod(10, 7)

print("divmod type: ", type(tmp) ," result: ", tmp)
print("lambda test: ", func(10))

set_test = {0,1,2,3,0}
print(set_test)
tuple_test = 0,1,2,3,4,0
print(tuple_test)