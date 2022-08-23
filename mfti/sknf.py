#sknf
sknf = [('0', '0', '0', '0', '0'), ('0', '0', '0', '0', '1'), ('0', '0', '0', '1', '0'), ('0', '0', '1', '0', '0'), ('0', '0', '1', '0', '1'), ('0', '0', '1', '1', '0'), ('0', '1', '0', '0', '0'), ('0', '1', '0', '1', '0'), ('0', '1', '1', '0', '0'), ('0', '1', '1', '1', '0'), ('1', '0', '0', '0', '0'), ('1', '0', '0', '1', '0'), ('1', '0', '1', '0', '0'), ('1', '0', '1', '1', '0'), ('1', '1', '0', '0', '0'), ('1', '1', '1', '0', '0')]
sknf_view = ""
for elm in sknf:
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
	#print(res_str)

print(sknf_view)