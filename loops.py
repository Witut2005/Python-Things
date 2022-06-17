
i = 0

while True:
    if i > 100:
        break
    print(i, end = "\n")
    i += 1



print("all parity numbers: ", end = "\n")

i = 0
while i <= 100:

    i += 1
    if i & 1:
        continue

    print(i, end = "\n")


