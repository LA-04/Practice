def Bit(x, make):
    k = 0
    plus = "++"
    mines = "--"
    for i in range(x):
        if plus in make[i][0].lower() and len(make[i][0]) == 3:
            k += 1
        elif mines in make[i][0].lower() and len(make[i][0]) == 3:
            k -= 1
    return k


x = int(input())
make = []
for i in range(x):
    make.append(input().split())

print(Bit(x, make))



