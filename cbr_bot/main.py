import requests
import xmltodict
import pprint
import json
from lxml import etree
from datetime import datetime
import telebot
from auth_data import token

def get_data(valute,date):
    try:

        req = requests.get(f"https://cbr.ru/scripts/XML_daily.asp?date_req={date}")
        xlm = req.content
        response = json.dumps(xmltodict.parse(xlm), indent=2, ensure_ascii=False)
        rec_json = json.loads(response)
        valutes = rec_json["ValCurs"]["Valute"]
        valutes_on_today = {info['Name']:info['Value'] for info in valutes}

        #     if info['CharCode'] == valute:
        #         rate = info['Value']
        #         name = info['Name']
        # print(f"Дата: {date}\nКурс {name}: {rate}" )
        print(valutes_on_today)
        print(rec_json)
    except Exception as ex:
        print(ex)
        print("Проверьте валюту и дату")


def main():
    valute = input("Введите валюту: ").upper()
    date = input("Введите дату дд/мм/гггг: ")
    get_data(valute, date)


# def telegram_bot(token):
#     bot = telebot.TeleBot(token)
#
#     @bot.message_handler(command=["start"])
#     def start_message(message):
#         bot.send_message(message.chat.id, "Добрый день, укажите дату и желаемую валюту")
#
#     bot.polling(none_stop = True)


if __name__ == '__main__':
    main()
    #telegram_bot(token)