def even_number(a):
    return a if a % 2 != 0 else False

k = list(map(int, input().split()))
lst = []
for a in k:
    if even_number(a):
        lst.append(a)
print(*lst)