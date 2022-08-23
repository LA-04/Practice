import json
import os
from PIL import Image
import pymysql
from config import host, user, password, db_name

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

            for row in rows:
                product_group = row.get("product")
                upload_wb = row.get("wb")

                if upload_wb == 0:
                    list_for_upload_wb.append(product_group)

            print(list_for_upload_wb)
            print("#" * 20)

            # 2
            select_all_rows = "SELECT * FROM wb_base_card;"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

            for row in rows:
                product_type = row.get("product_type")
                path_base_json = row.get("path_base_json")

                for product_for_upload in list_for_upload_wb:
                    if product_type in product_for_upload:

                        with open('testtempl.json', encoding='utf-8') as keys:
                            set_keys = json.load(keys)

                        with open(f'{path_base_json}', encoding='utf-8') as discription:
                            set_discription = json.loads(discription.read())

                        print(set_discription)

            print("#" * 20)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)