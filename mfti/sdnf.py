#sdnf
sdnf = [('0', '0', '0', '1', '1'), ('0', '0', '1', '1', '1'), ('0', '1', '0', '0', '1'), ('0', '1', '0', '1', '1'), ('0', '1', '1', '0', '1'), ('0', '1', '1', '1', '1'), ('1', '0', '0', '0', '1'), ('1', '0', '0', '1', '1'), ('1', '0', '1', '0', '1'), ('1', '0', '1', '1', '1'), ('1', '1', '0', '0', '1'), ('1', '1', '0', '1', '0'), ('1', '1', '0', '1', '1'), ('1', '1', '1', '0', '1'), ('1', '1', '1', '1', '0'), ('1', '1', '1', '1', '1')]
sdnf_view = ""
for elm in sdnf:
    tmp_str = ''.join(elm)
    res_str=""
    ind = 1
    for c in tmp_str:
        if c == '1':
            find_index = tmp_str.find(c)
            res_str += 'x' + str(find_index+ind)
            tmp_str = tmp_str[:find_index] + tmp_str[(find_index+1):]
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
	#print(res_str)

print(sdnf_view)