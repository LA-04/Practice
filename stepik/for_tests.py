def get_rect_value(a, b, type=0):
    if type == 0:
        return 2*(a+b)
    else:
        return a*b

#numbers = list(map(int, input().split()))
print(get_rect_value(2, 4))