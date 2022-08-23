import itertools

a = 0
fict = 0
nf = []
print("Количество переменных:")
args = int(input())
while True:
    print('Значение функции:')
    func = input()
    if 2 ** args == len(func):
        break
for i in itertools.product('01', repeat=args):
    nf.append(i)
    nf.extend(func[a])
    print(' '.join(i) + '  ' + func[a])
    print('-----------')
    fict += int(func[a])
    a += 1

matr = list(func)
b = None
iter = 1
check = 0
if fict % 2 != 0:
    print("There is no fictitious variables")
if fict % 2 == 0:
    for k in range(args):

        for s in range(2 ** check):

            if matr[:int((2 ** args) / 2 ** iter)] == matr[int((2 ** args) / 2 ** iter): int(
                    ((2 ** args) / 2 ** iter) + (2 ** args) / 2 ** iter)]:
                del matr[:int(((2 ** args) / 2 ** iter) + (2 ** args) / 2 ** iter)]

        if len(matr) == 0:
            print(f' Фиктивная переменная x{k+1}')

        check += 1
        iter += 1
        matr = list(func)
for i, item in enumerate(nf):
    if item == 0:
        del item
print(nf)