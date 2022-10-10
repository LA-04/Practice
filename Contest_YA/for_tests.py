def datas(day):
    days = range(1, 32)
    months = range(1, 32)
    years = range(1970, 2070)
    if day[0] in days and day[1] in months and day[2] in years:
        if day[0] <= 12 and day[1] <= 12 and day[0] != day[1]:
            return 0
        else:
            return 1


# day = list(map(int, input().split()))
# print(datas(day))

print(datas([1, 2, 2003]))  # 0
print(datas([7, 12, 2003]))  # 0
print(datas([7, 13, 2003]))  # 1
print(datas([13, 2, 2003]))  # 1
print(datas([21, 22, 2003]))  # 0
print(datas([12, 12, 2003]))  # 0
print(datas([1, 12, 2003]))  # 0
print(datas([12, 12, 2003]))  # 1