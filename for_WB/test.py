import requests
import json
from requests.structures import CaseInsensitiveDict


#url = "https://api-seller.ozon.ru/v2/product/info"
url_1 = "https://api-seller.ozon.ru/v3/products/info/attributes"
url_2 = "https://api-seller.ozon.ru/v2/category/attribute/values"

headers = CaseInsensitiveDict()
headers["Client-Id"] = "287318"
headers["Api-Key"] = "0f6afa92-d026-47da-b951-d1198bf31ce7"
headers["Content-Type"] = "application/json"

data = """
{
    "filter": {
    "offer_id": [
         "base_notepad_sketch-0"
         ],
    "visibility": "ALL"
    },
    "limit": 100,
    "sort_dir": "ASC"

}
"""
data_atr = """
{
    "attribute_id": 8229,
    "category_id": 27342505,
    "language": "DEFAULT",
    "last_value_id": 0,
    "limit": 3
}
"""
# "offer_id": [
#         "base_notepad_sketch-0"
#         ],
# "product_id":
# [
#     "320479152"
# ],
# "language":"EN"
resp = requests.post(url_1, headers=headers, data=data)
atr = requests.post(url_2, headers=headers, data=data_atr)

with open(f'atr_cards.json', 'w', encoding='utf8') as ID_ozon:
    json.dump(resp.json(), ID_ozon, indent=2, ensure_ascii=False)

with open(f'attribute.json', 'w', encoding='utf8') as atr_ozon:
    json.dump(atr.json(), atr_ozon, indent=2, ensure_ascii=False)

print(resp.status_code, atr.status_code)
