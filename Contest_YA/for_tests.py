def csickl_sdvig(a):
    tmp = a[0]
    for k in range(len(a) - 1):
        a[k] = a[k + 1]
    a[len(a) - 1] = tmp
    return a


a = [1,2,3,4,5]
print(csickl_sdvig(a))

