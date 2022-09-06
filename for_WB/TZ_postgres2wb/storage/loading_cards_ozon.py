import json
import os
from PIL import Image
import pymysql
from config import host, user, password, db_name
import requests
from requests.structures import CaseInsensitiveDict
from loguru import logger


def upload_list(cursor):
    select_all_rows = "SELECT * FROM upload_list;"
    cursor.execute(select_all_rows)
    rows = cursor.fetchall()
    list_for_upload_ozon = []

    for row in rows:
        product_group = row.get("product")
        upload_ozon = row.get("ozon")

        if upload_ozon == 0:
            list_for_upload_ozon.append(product_group)

    logger.info("Список продуктов к загрузке сформирован...", 1)
    return list_for_upload_ozon


def request_on_ozon(list_for_upload):
    t = {
        "filter": {
        "offer_id": [
             "base_notepad_clear-0"
             ],
        "visibility": "ALL"
        },
        "limit": 100,
        "sort_dir": "ASC"
    }

    p = t.get("filter")

    for i, values in enumerate(list_for_upload):
        p.update({"offer_id": [values]})
        print(t)
        url_1 = "https://api-seller.ozon.ru/v3/products/info/attributes"

        headers = CaseInsensitiveDict()
        headers["Client-Id"] = "287318"
        headers["Api-Key"] = "0f6afa92-d026-47da-b951-d1198bf31ce7"
        headers["Content-Type"] = "application/json"

        data = f"""{json.dumps(t, indent=2, ensure_ascii=False)}""".encode('utf8')
        resp = requests.post(url_1, headers=headers, data=data)
        status = resp.status_code
        if status == 200:
            logger.info("Карточка с озона получена...", 1)
            re_json = resp.json()
            with open(f'request_to_oz\\{values}_oz.json', 'w', encoding='utf8') as dis_WB:
                json.dump(re_json, dis_WB, indent=2, ensure_ascii=False)
            # print(resp_json)
        else:
            logger.error(f"Ошибка {status} - Карточка с озона не получена...", 1)
        return re_json


def return_values(resp_json):
    open_atrib = resp_json.get("result")
    atrib = open_atrib[0].get("attributes")
    # print(atrib)

    with open('templates\\insert_card_oz.json', encoding='utf-8') as insert_card:
        set_insert_card = json.load(insert_card)

    open_atrib_insert = set_insert_card.get("result")
    atrib_insert = open_atrib_insert[0].get("attributes")

    for key, value_key in enumerate(atrib):
        for ket_insert, value_key_insert in enumerate(atrib_insert):

            if value_key['attribute_id'] == value_key_insert['attribute_id'] and value_key['values'] != \
                    value_key_insert['values']:
                value_key['values'] = value_key_insert['values']

    # print(atrib)
    open_atrib[0].update({"attributes": atrib})
    resp_json.update({"result": open_atrib})
    # print(resp_json)
    logger.info("Замена значений произведена успешно...", 1)
    return resp_json


def send_to_ozon(return_json):
    open_atrib = return_json.get("result")
    atrib = open_atrib[0].get("attributes")
    with open(f'atrib_cards_with_insert.json', 'w', encoding='utf8') as cards_with_insert:
        json.dump(return_json, cards_with_insert, indent=2, ensure_ascii=False)
    asd = {"attributes": atrib}
    items = {"items": [asd]}
    with open(f'items_cards_with_insert.json', 'w', encoding='utf8') as cards_with_insert:
        json.dump(items, cards_with_insert, indent=2, ensure_ascii=False)
    # print(items)
    headers = CaseInsensitiveDict()
    headers["Client-Id"] = "287318"
    headers["Api-Key"] = "0f6afa92-d026-47da-b951-d1198bf31ce7"
    headers["Content-Type"] = "application/json"

    url_2 = "https://api-seller.ozon.ru/v2/product/import"
    data = f"""{json.dumps(items, indent=2, ensure_ascii=False)}""".encode('utf8')

    resp_ex = requests.post(url_2, headers=headers, data=data)
    status = resp_ex.status_code
    if status == 200:
        logger.info("Обновленная карточка на озон отправлена...", 1)
    else:
        logger.error(f"Ошибка {status} - Обновленная карточка на озон не отправлена...", 1)


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    logger.info("Подключение к бд успешно...", 1)
    try:
        with connection.cursor() as cursor:

            list_for_upload = upload_list(cursor)

            resp_json = request_on_ozon(list_for_upload)

            return_json = return_values(resp_json)

            send_json = send_to_ozon(return_json)

    finally:
        connection.close()

except Exception as ex:
    logger.error("Подключение к бд не удалось...", 1)
    print(ex)