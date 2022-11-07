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
            print(rows)
            list_for_upload_wb = []
            list_for_upload_ozon = []

            for row in rows:
                product_group = row.get("product")
                upload_wb = row.get("wb")
                upload_ozon = row.get("ozon")

                if upload_wb == 0:
                    list_for_upload_wb.append(product_group)

                if upload_ozon == 0:
                    list_for_upload_ozon.append(product_group)

            print(list_for_upload_wb)
            print(list_for_upload_ozon)
            print("#" * 20)

            # 2.2
            # Заходим в таблицу wb_base_card для поиска пути джесона
            select_all_rows = "SELECT * FROM wb_base_card;"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

            for row in rows:
                product_type = row.get("product_type")
                path_insert_json = row.get("path_insert_json")

                for product_for_upload in list_for_upload_wb:
                    if product_type in product_for_upload:

                        with open('templates\\testtempl.json', encoding='utf-8') as keys:
                            set_keys = json.load(keys)

                        with open(f'insert_fields\\insert_{product_type}.json', encoding='utf-8') as discription:
                            set_discription = json.loads(discription.read()).get("addin")

                        for num, value in enumerate(set_discription):
                            params = value.get("params")
                            repl = params[0]["value"]

                            for key, value_key in reversed(set_keys.items()):
                                if key in repl:
                                    repl = repl.replace(f'{key}', value_key)

                            value["params"][0].update({"value":repl})

                        with open(f'product_with_keys\\{product_type}_with_keys.json', 'w', encoding='utf8') as dis_WB:
                            json.dump(set_discription, dis_WB, ensure_ascii=False)
            print("Files uploaded!")
            print("#" * 20)

            # 2.3

            select_all_rows = "SELECT * FROM wb_base_card;"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

            for row in rows:
                product_type = row.get("product_type")
                path_base_json = row.get("path_base_json")

                for product_for_upload in list_for_upload_wb:
                    if product_type in product_for_upload:

                        with open(f"product_with_keys\\{product_type}_with_keys.json", encoding="utf-8") as product_with_keys:
                            informs_for_replace = json.loads(product_with_keys.read())

                        with open(f"base_cards\\base_{product_type}.json", encoding="utf-8") as base_product_json:
                            full_json_for_inform_replace = json.loads(base_product_json.read())

                        json_for_inform_replace = full_json_for_inform_replace.get("addin")

                        for num_inf, value_inform in enumerate(informs_for_replace):
                            for num_js, value_json in enumerate(json_for_inform_replace):
                                if value_inform.get("type") == value_json.get("type"):
                                    json_for_inform_replace[num_js] = value_inform
                        full_json_for_inform_replace.update({"addin": json_for_inform_replace})

                        with open(f"json_with_inf\\{product_type}_with_inf.json", "w", encoding="utf8") as dis_WB:
                            json.dump(full_json_for_inform_replace, dis_WB, ensure_ascii=False)

            print("Files uploaded!")
            print("#" * 20)

            # 3


    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)