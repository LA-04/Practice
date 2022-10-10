def arbu(kg):
    if 4 <= kg <= 100 and kg % 2 == 0:
        return "YES"
    else:
        return "NO"

print(arbu(int(input())))
