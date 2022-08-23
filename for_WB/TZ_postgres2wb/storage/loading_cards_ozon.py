import json
import os
from PIL import Image
import pymysql
from config import host, user, password, db_name
import requests
from requests.structures import CaseInsensitiveDict



# try:
#     connection = pymysql.connect(
#         host=host,
#         port=3306,
#         user=user,
#         password=password,
#         database=db_name,
#         cursorclass=pymysql.cursors.DictCursor
#     )
#     print("successfully connected...")
#     print("#" * 20)
#     try:
#         with connection.cursor() as cursor:
#
#             # 1 пункт, проходим по листу загрузок, если не загружен, формируем список с продуктами к загрузке
#             select_all_rows = "SELECT * FROM upload_list;"
#             cursor.execute(select_all_rows)
#             rows = cursor.fetchall()
#             list_for_upload_ozon = []
#
#             for row in rows:
#                 product_group = row.get("product")
#                 upload_ozon = row.get("ozon")
#
#                 if upload_ozon == 0:
#                     list_for_upload_ozon.append(product_group)
#
#             print(list_for_upload_ozon)
#             print("#" * 20)

            #отправка запроса на получение карточки из озона

url_1 = "https://api-seller.ozon.ru/v3/products/info/attributes"

headers = CaseInsensitiveDict()
headers["Client-Id"] = "287318"
headers["Api-Key"] = "0f6afa92-d026-47da-b951-d1198bf31ce7"
headers["Content-Type"] = "application/json"

t = """{
    "filter": {
    "offer_id": [
         "base_notepad_sketch-0"
         ],
    "visibility": "ALL"
    },
    "limit": 100,
    "sort_dir": "ASC"

}"""

data = t

resp = requests.post(url_1, headers=headers, data=data)
print(resp.status_code)
resp_json = resp.json()
print(resp_json)

open_atrib = resp_json.get("result")
atrib = open_atrib[0].get("attributes")
print(atrib)

with open('templates\\insert_card_oz.json', encoding='utf-8') as insert_card:
    set_insert_card = json.load(insert_card)

open_atrib_insert = set_insert_card.get("result")
atrib_insert = open_atrib_insert[0].get("attributes")

for key, value_key in enumerate(atrib):
    for ket_insert, value_key_insert in enumerate(atrib_insert):

        if value_key['attribute_id'] == value_key_insert['attribute_id'] and value_key['values'] != value_key_insert['values']:
            value_key['values'] = value_key_insert['values']


#     print(value_key)
print(atrib)
open_atrib[0].update({"attributes":atrib})
resp_json.update({"result":open_atrib})
print(resp_json)
# print(atrib_insert)
with open(f'atrib_cards_with_insert.json', 'w', encoding='utf8') as cards_with_insert:
    json.dump(resp_json, cards_with_insert, indent=2, ensure_ascii=False)
asd = {"attributes":atrib}
items = {"items" : [asd]}
with open(f'items_cards_with_insert.json', 'w', encoding='utf8') as cards_with_insert:
    json.dump(items, cards_with_insert, indent=2, ensure_ascii=False)
print(items)


url_2 = "https://api-seller.ozon.ru/v2/product/import"
data = f"""{items}""".encode('utf8')
# data = """{
# "items": [
# {
# "attributes": [
# {
# "attribute_id": 8229,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 96168,
#   "value": "Скетчбук красивый"
# }
# ]
# },
# {
# "attribute_id": 6532,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "56"
# }
# ]
# },
# {
# "attribute_id": 6531,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "12232"
# }
# ]
# },
# {
# "attribute_id": 5254,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 56844,
#   "value": "Разметка линеечная"
# }
# ]
# },
# {
# "attribute_id": 5260,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 12201,
#   "value": "Кольца красные"
# }
# ]
# },
# {
# "attribute_id": 5257,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 970885687,
#   "value": "Стальная бумага"
# }
# ]
# },
# {
# "attribute_id": 9997,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 970663854,
#   "value": "Веселый"
# },
# {
#   "dictionary_value_id": 970663847,
#   "value": "Расстения"
# }
# ]
# },
# {
# "attribute_id": 8966,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 970905212,
#   "value": "Дайвинг и путешествия"
# }
# ]
# },
# {
# "attribute_id": 5261,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 12770,
#   "value": "В линейку с полями"
# }
# ]
# },
# {
# "attribute_id": 10097,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "color0"
# }
# ]
# },
# {
# "attribute_id": 9024,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "base_notepad_sketch-0"
# }
# ]
# },
# {
# "attribute_id": 85,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 971224781,
#   "value": "YOUNI"
# }
# ]
# },
# {
# "attribute_id": 4191,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "Творческая тетрадь С ЛЯГУШОНКОМ ( скетчбук, блокнот скечбук ) от компании YOUni - оригинальный канцтовар для школы, в университет, на работу; подарок для мальчика, подарок для девочки, для друга или подруги. Арт блокнот С ЛЯГУШКАМИ можно использовать как блокнот для записей, блокнот для рисования, блокнот для заметок, блокнот для скетчинга. Творческий блокнот для рисования идеален для подарка на Новый год, День рождения, 14 февраля, 23 февраля или 8 марта тем, кто любит ЛЯГУШЕК. Обложка арт блокнота на пружине не твердая, но плотная, с глянцевой ламинацией. Листы рабочей тетради на пружине белые, без линовки (нелинованные). Плотность бумаги блокнота без линовки - 160 гр/м2. В ассортименте также имеются тетради в линейку, тетради в клетку, тетради в точку, тетради 48 и другие канцтовары для школы. Погрузитесь в особую атмосферу с продукцией от YOUni! Создайте свою вселенную!"
# }
# ]
# },
# {
# "attribute_id": 4389,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 90295,
#   "value": "Россия"
# }
# ]
# },
# {
# "attribute_id": 11794,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 970860783,
#   "value": "safe"
# }
# ]
# },
# {
# "attribute_id": 13216,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 971006037,
#   "value": "Унисекс"
# }
# ]
# },
# {
# "attribute_id": 10015,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "false"
# }
# ]
# },
# {
# "attribute_id": 21702,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 82353,
#   "value": "Нет"
# }
# ]
# },
# {
# "attribute_id": 5258,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 12066,
#   "value": "Без ограничения"
# }
# ]
# },
# {
# "attribute_id": 10100,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "false"
# }
# ]
# },
# {
# "attribute_id": 21807,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 971229788,
#   "value": "A5 (14.8 × 21 см)"
# }
# ]
# },
# {
# "attribute_id": 9048,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "base_notepad_sketch"
# }
# ]
# },
# {
# "attribute_id": 9461,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 349827741,
#   "value": "Скетчбук"
# }
# ]
# },
# {
# "attribute_id": 4180,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "YOUni / Скетчбук с лягушкой для рисования / Блокнот с лягушечкой для скетчинга"
# }
# ]
# },
# {
# "attribute_id": 22074,
# "complex_id": 0,
# "values": [
# {
#   "dictionary_value_id": 0,
#   "value": "false"
# }
# ]
# }
# ]
# }
# ]
# }""".encode('utf8')

resp_ex = requests.post(url_2, headers=headers, data=data)
print(resp_ex.status_code)



#     finally:
#         connection.close()
#
# except Exception as ex:
#     print("Connection refused...")
#     print(ex)