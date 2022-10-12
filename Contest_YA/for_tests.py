def matrix(m):
    for i, item in enumerate(m):
        for j, jtem in enumerate(item):
            if jtem == 1:
                row = abs(i - 2)
                st = abs(j - 2)
                return row + st


m = []
for i in range(5):
    m.append(list(map(int, input().split())))

print(matrix(m))




