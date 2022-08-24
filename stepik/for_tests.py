def even_number(a):
    return a if a % 2 == 0 else False

a = int(input())
while a != 1:
    if even_number(a):
        print(a)
    a = int(input())