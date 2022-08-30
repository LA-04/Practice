import requests
from datetime import datetime
import telebot
from auth_data import token

def get_data(valute,date):
    try:
        req = requests.get(f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js")
        response = req.json()
        eur = response["Valute"][f"{valute}"]["Value"]
        print(f"Дата: {date}\nКурс ЕВРО: {eur}" )
    except Exception as ex:
        print(ex)
        print("Проверьте валюту и дату")


def main():
    valute = input("Введите валюту: ").upper()
    date = input("Введите дату гггг/мм/дд : ")
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