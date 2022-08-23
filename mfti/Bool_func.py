import itertools

def


a = 0
fict = 0
sdnf = []
sknf = []
num_func = int(input())

# Указываем количество переменных
print("Количество переменных:")
args = int(input())

# Указываем знаечение функции
while True:
    print('Значение функции:')
    func = input()
    if 2 ** args == len(func):
        break

# Цикл для заполнения массива СДНФ и СКНФ а так же вывода таблицы истинности
for i in itertools.product('01', repeat=args):
    if func[a] != '0':
        sdnf.append(i)
    else:
        sknf.append(i)
    print(' '.join(i) + '  ' + func[a])
    print('-----------')
    fict += int(func[a])
    a += 1


matr = list(func)
del_matr = list(func)
iter = 1
check = 0

# Проверка на наличие фиктивной переменной
if fict % 2 == 0:
    for k in range(args):
        for s in range(2 ** check):
            if matr[:int((2 ** args) / 2 ** iter)] == matr[int((2 ** args) / 2 ** iter): int(
                    ((2 ** args) / 2 ** iter) + (2 ** args) / 2 ** iter)]:

                del matr[:int(((2 ** args) / 2 ** iter) + (2 ** args) / 2 ** iter)]

        if len(matr) == 0:
            t = int((2 ** args) / (2 ** (k + 1)))

            # Цикл для удаления значений функции
            for i in range(1, t + 1):
                l = t * i
                del del_matr[l:t + l]

            print(f"Фиктивная переменная: X{k + 1}")
            print(f"Функция без фективной переменной: {del_matr}")
        check += 1
        iter += 1
        matr = list(func)


print(sdnf)
print(sknf)

#00010001010101010101010101110111
#0001010101010111