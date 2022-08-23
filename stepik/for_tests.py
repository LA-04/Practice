def max_min_summ(x):
    print(f'Min = {min(x)}, max = {max(x)}, sum = {sum(x)}')


max_min_summ(list(map(int, input().split())))
