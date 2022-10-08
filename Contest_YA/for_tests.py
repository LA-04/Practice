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


print(interactor(0,0,0))
print(interactor(-1,0,1))
print(interactor(42,1,6))
print(interactor(44,7,4))
print(interactor(1,4,0))
print(interactor(-3,2,4))