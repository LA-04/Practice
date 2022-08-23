import itertools

def param_func():

    # Указываем количество переменных
    print("Количество переменных:")
    args.append(int(input()))

    # Указываем знаечение функции
    print('Значение функции:')
    func.append(list(input()))
    for i in range(len(func)):
        if 2 ** args[i] != len(func[i]):
            break
    #return args,func


def sdnf_f():
    sdnf_view = ""
    for index_sdnf, mass_sdnf in enumerate(sdnf):
        for elm in mass_sdnf:
            tmp_str = ''.join(elm)
            res_str = ""
            ind = 1
            for c in tmp_str:
                if c == '1':
                    find_index = tmp_str.find(c)
                    res_str += 'x' + str(find_index + ind)
                    tmp_str = tmp_str[:find_index] + tmp_str[(find_index + 1):]
                    ind = ind + 1
                else:
                    find_index = tmp_str.find(c)
                    res_str += '~x' + str(find_index + ind)
                    tmp_str = tmp_str[:find_index] + tmp_str[(find_index + 1):]
                    ind = ind + 1
            if len(sdnf_view) == 0:
                sdnf_view = sdnf_view + res_str
            else:
                sdnf_view = sdnf_view + '^' + res_str
    print(sdnf_view)


def sknf_f():
    sknf_view = ""
    for index_sknf, mass_sknf in enumerate(sknf):
        for elm in mass_sknf:
            tmp_str = ''.join(elm)
            res_str = ""
            ind = 1
            for c in tmp_str:
                if c == '0':
                    find_index = tmp_str.find(c)
                    res_str += 'x' + str(find_index + ind)
                    tmp_str = tmp_str[:find_index] + tmp_str[(find_index + 1):]
                    ind = ind + 1
                else:
                    find_index = tmp_str.find(c)
                    res_str += '~x' + str(find_index + ind)
                    tmp_str = tmp_str[:find_index] + tmp_str[(find_index + 1):]
                    ind = ind + 1
            if len(sknf_view) == 0:
                sknf_view = sknf_view + res_str
            else:
                sknf_view = sknf_view + 'v' + res_str
    print(sknf_view)


a = 0
fict = 0
q = 0
sdnf = []
sdnf_tmp = []
sknf_tmp = []
sknf = []
args = []
func = []
num_func = int(input("Количество функций"))

for i in range(num_func):
    param_func()

while q < num_func:
        args_i = args[q]
        func_i = func[q]
        a = 0
        sdnf_tmp = []
        sknf_tmp = []
        for i in itertools.product('01', repeat=args_i):
            if func_i[a] != '0':
                sdnf_tmp.append(i)
            else:
                sknf_tmp.append(i)
            a += 1
            sdnf.append(sdnf_tmp)
            sknf.append(sknf_tmp)
        q += 1




sknf_view = ""
for index_sknf, mass_sknf in enumerate(sknf):
    for elm in mass_sknf:
        tmp_str = ''.join(elm)
        res_str=""
        ind = 1
        for c in tmp_str:
            if c == '0':
                find_index = tmp_str.find(c)
                res_str += 'x' + str(find_index+ind)
                tmp_str = tmp_str[:find_index] + tmp_str[(find_index+1):]
                ind = ind + 1
            else:
                find_index = tmp_str.find(c)
                res_str += '~x' + str(find_index + ind)
                tmp_str = tmp_str[:find_index] + tmp_str[(find_index + 1):]
                ind = ind + 1
        if len(sknf_view) == 0:
            sknf_view = sknf_view + res_str
        else:
            sknf_view = sknf_view + 'v' + res_str



print(args)
print(func)
print(sdnf)
sdnf_f()
print(sknf)
sknf_f()
#00010001010101010101010101110111
#0001010101010111