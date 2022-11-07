def tri(d, x):
    if d <= 1000:
        if 0 <= x[0] <= d and 0 <= x[1] <= d and (x[0] * x[1] <= (d^2 // 2)):
            return 0
        elif (x[0] < 0 or x[1] < 0) and (abs(x[0]) == abs(x[1])):
            return 1
        elif (x[0] > d // 2 and x[1] < d // 2):
            return 3
        elif (x[0] < d // 2 and x[1] > d // 2) or (x[0] == x[1]):
            return 2


# d = int(input())
# x = list(map(int, input().split()))
#
# print(tri(d, x))

print(tri(5, [1,1]))
print(tri(3, [-1,-1]))
print(tri(4, [4,4]))
print(tri(4, [2,2]))
print(tri(4, [3,3]))
print(tri(4, [-1,3])) #3
print(tri(4, [-2,2])) #1
print(tri(4, [-3,1])) #1
print(tri(4, [3,-1])) #2