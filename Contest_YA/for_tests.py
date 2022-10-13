def schools(students, coordinates):
    if 0 < students < 100001:
        middle = sum(coordinates)
        if middle >= 0:
            return middle // students
        else:
            return middle // students + 1


# students = int(input())
# coordinates = list(map(int, input().split()))
#
# print(schools(students, coordinates))

print(schools(4,[1,2,3,4]))
print(schools(3,[-1,0,1]))
print(schools(3,[5,7,9]))
print(schools(2,[0,1]))
print(schools(3,[-100,0,1]))
print(schools(0,[]))
print(schools(3,[8,3,4]))
print(schools(3,[-11,0,1]))