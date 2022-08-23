import pandas as pd

gears = pd.read_excel('nmrv.xlsx')

print('Введите название редуктора')
what_gear = input()
print('Какой пам?')
PAM = str(input())
print('Передаточное')
ratio = int(input())

for words, numbers in enumerate(what_gear):
        if numbers.isdigit():
                name = what_gear[:words]
                size = int(what_gear[words:])
                break

type_gear = gears.loc[gears['name'] == name]
size_gear = type_gear.loc[type_gear['size'] == size]
what_PAM = size_gear.loc[size_gear['PAM'] == PAM]
what_ratio = what_PAM.loc[what_PAM['Ratio (i)'] == ratio]

print(size_gear)
input()
print(what_PAM)
input()
print(what_ratio)