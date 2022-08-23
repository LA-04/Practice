import json

with open('testtempl.json', encoding='utf-8') as keys:
    set_keys = json.load(keys)

with open('insert_notepad_line.json', encoding='utf-8') as discription:
    set_discription = json.loads(discription.read())

print(set_keys)
print(set_discription)

for key_d, i in set_discription.items():
    for p, t in enumerate(i):
        for k, m in t.items():
            if k != 'params':
                continue
            for w, o in enumerate(m):
                for l, f in o.items():
                    for key, j in set_keys.items():
                        b = f.split()
                        for x in b:
                            if "." or "," or "/" in x:
                                x = x.replace(".", "")
                                x = x.replace(",", "")
                                x = x.replace("/", "")
                            if key == x:
                                print(key)
                                print(j)
                                f = f.replace(f"{key}", j)


                print(f)
            o[l] = f
print(set_discription)
with open('dis_wb.json','w', encoding='utf8') as dis_WB:
    json.dump(set_discription, dis_WB, ensure_ascii = False)
