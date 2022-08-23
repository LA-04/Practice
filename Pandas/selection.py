import pandas as pd

df = pd.read_excel('nmrv.xlsx')

types = dict(червячный=set(df['name'].tolist()), соосный=['h', 'ha', 'hfa'])
sizes = dict(червячный=set(df['size'].tolist()), соосный=[42, 52, 62])

select = input()


#этот цикл разбивает строку на буквы и цифры
for words, numbers in enumerate(select):
        if numbers.isdigit():
                name = select[:words]
                size = int(select[words:])
                break
#этот цикл определяет тип редуктора
for type, names in types.items():
        for version in names:
                if name == version:
                        a = type
#этот цикл определяет габарит редуктора
for type, sizes in sizes.items():
        for dimention in sizes:
                if dimention == size and a == type:
                        print("Тип редуктора:", a,"\nГабарит:", dimention)


