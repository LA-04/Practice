def interactor(end_cod,verd_inter,verd_check):
    checker = range(8)
    inter = range(8)
    info = range(-128,128)
    if end_cod in info and verd_inter in inter and verd_check in checker:
        if verd_inter == 0 and end_cod != 0:
            return 3
        elif verd_inter == 0:
            return verd_check
        if verd_inter == 1:
            return verd_check
        if verd_inter == 4 and end_cod != 0:
            return 3
        elif verd_inter == 4:
            return 4
        if verd_inter == 6:
            return 0
        if verd_inter == 7:
            return 1
        else:
            return verd_inter


a = int(input())
b = int(input())
c = int(input())

print(interactor(a,b,c))