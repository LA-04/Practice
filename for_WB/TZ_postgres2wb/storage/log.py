import json

name = "insert_cup_white"

with open(f"templates\\{name}.json", encoding="utf-8") as insert_card_ozon:
    insert_card_without_keys = json.loads(insert_card_ozon.read())

with open(f'request_to_oz\\{values[9:-2]}_from_ozon.json', 'w', encoding='utf8') as dis_WB:
    json.dump(re_json, dis_WB, indent=2, ensure_ascii=False)

