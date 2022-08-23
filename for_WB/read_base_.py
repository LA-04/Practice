import json

with open('dis_wb.json', encoding='utf-8') as dis_wb:
    set_dis_wb = json.loads(dis_wb.read())

with open('base_notepad_line.json', encoding='utf-8') as base:
    set_base = json.loads(base.read())

for key_base, i in set_base.items():
    if key_base != "addin":
        continue
    for ind, per in enumerate(i):
        for type_base, val_base in per.items():
            if type_base != "type":
                continue
            for key_ins, k in set_dis_wb.items():
                for per_ins in k:
                    for type_ins, val_ins in per_ins.items():
                        if type_ins == type_base and val_ins == val_base:
                            i[ind] = per_ins
print(set_base)
# with open('ins_wb.json','w', encoding='utf8') as ins_WB:
#     json.dump(set_base, ins_WB, ensure_ascii = False)