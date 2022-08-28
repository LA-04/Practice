import json
import os
from PIL import Image
import pymysql
from config import host, user, password, db_name
import requests
from requests.structures import CaseInsensitiveDict



try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
    try:
        with connection.cursor() as cursor:

            # 1 пункт, проходим по листу загрузок, если не загружен, формируем список с продуктами к загрузке
            select_all_rows = "SELECT * FROM upload_list;"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            list_for_upload_ozon = []

            for row in rows:
                product_group = row.get("product")
                upload_ozon = row.get("ozon")

                if upload_ozon == 0:
                    list_for_upload_ozon.append(product_group)

            print("Список продуктов к загрузке сформирован...")
            print("#" * 20)

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
            status = resp.status_code
            if status == 200:
                print("Карточка с озона получена...")
                print("#" * 20)
                resp_json = resp.json()
                #print(resp_json)
            else:
                print(f"Ошибка {status} - Карточка с озона не получена...")
            open_atrib = resp_json.get("result")
            atrib = open_atrib[0].get("attributes")
            #print(atrib)

            with open('templates\\insert_card_oz.json', encoding='utf-8') as insert_card:
                set_insert_card = json.load(insert_card)

            open_atrib_insert = set_insert_card.get("result")
            atrib_insert = open_atrib_insert[0].get("attributes")

            for key, value_key in enumerate(atrib):
                for ket_insert, value_key_insert in enumerate(atrib_insert):

                    if value_key['attribute_id'] == value_key_insert['attribute_id'] and value_key['values'] != value_key_insert['values']:
                        value_key['values'] = value_key_insert['values']

            #print(atrib)
            open_atrib[0].update({"attributes":atrib})
            resp_json.update({"result":open_atrib})
            #print(resp_json)
            print("Замена значений произведена успешно...")
            print("#" * 20)

            with open(f'atrib_cards_with_insert.json', 'w', encoding='utf8') as cards_with_insert:
                json.dump(resp_json, cards_with_insert, indent=2, ensure_ascii=False)
            asd = {"attributes":atrib}
            items = {"items" : [asd]}
            with open(f'items_cards_with_insert.json', 'w', encoding='utf8') as cards_with_insert:
                json.dump(items, cards_with_insert, indent=2, ensure_ascii=False)
            #print(items)

            url_2 = "https://api-seller.ozon.ru/v2/product/import"
            data = f"""{json.dumps(items, indent=2, ensure_ascii=False)}""".encode('utf8')

            resp_ex = requests.post(url_2, headers=headers, data=data)
            status = resp_ex.status_code
            if status == 200:
                print("Обновленная карточка на озон отправлена...")
                print("#" * 20)
            else:
                print(f"Ошибка {status} - Обновленная карточка на озон не отправлена...")



    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)