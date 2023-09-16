rows=int(input("введите число рядов: "))
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print("")