def sity(sitys):
    d = {town: len(town) for town in sitys}
    return d

sitys = list(map(str, input().split()))
d = sity(sitys)
a = sorted(d, key=lambda x: d[x])
print(*a)