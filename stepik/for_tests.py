def perimetr(width, heigth):
    print(f'Периметр прямоугольника, равен {2*(width+heigth)}')

width, heigth = map(int, input().split())
perimetr(width, heigth)