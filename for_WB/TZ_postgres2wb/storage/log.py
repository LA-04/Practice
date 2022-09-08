import json

name = "insert_cup_white"

with open(f"templates\\{name}.json", encoding="utf-8") as insert_card_ozon:
    insert_card_without_keys = json.loads(insert_card_ozon.read())

with open(f"templates\\keys.json", encoding="utf-8") as keys_ozon:
    keys_for_replase = json.loads(keys_ozon.read())

    for i, item in enumerate(insert_card_without_keys):
        values = item.get("values")
        value = values[0].get("value")
        for key, key_values in reversed(keys_for_replase.items()):
            if key in value:
                value = value.replace(f'{key}', key_values)
                values[0].update({"value": value})

with open(f'templates\\{name}_with_keys.json', 'w', encoding='utf8') as insert_card_with_keys:
    json.dump(insert_card_without_keys, insert_card_with_keys, indent=2, ensure_ascii=False)

