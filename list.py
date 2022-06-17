

var1 = 12345678
var2 = "string"


my_list = [var1, var2]

print("list content: ", end = "\n")

my_list += [my_list[0], my_list[1]]

print(my_list)

my_list.reverse()

print(my_list)

my_list.insert(0, "test")

my_list.append("end")

print(my_list)

my_list.append(["another", "list"])

print(my_list)

print(my_list[6][0])

print(len(my_list))


print("how much 12345678")
print(my_list.count(12345678))

print("its index", my_list.index(12345678))


my_list.remove(12345678)
print(my_list)