import requests
import datetime
from auth_data import token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


storage = MemoryStorage()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

class FSMAdmin(StatesGroup):
    valute = State()
    day = State()

#Начало диалога загрузки выбора валюты
@dp.message_handler(commands=["start"], state=None)
async def cm_start(message: types.Message):
    b1 = KeyboardButton('EUR')
    b2 = KeyboardButton('USD')
    b3 = KeyboardButton('JPY')
    b4 = KeyboardButton('CNY')

    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

    kb_client.add(b1).row(b2).add(b3).row(b4)

    await FSMAdmin.valute.set()
    await message.answer("Добрый день, выберете называние валюты:", reply_markup=kb_client)

#Получаем и сохраняем валюту
@dp.message_handler(state=FSMAdmin.valute)
async def valute_selection(message: types.Message, state: FSMContext):
    b1 = KeyboardButton('2021/05/01')
    b2 = KeyboardButton('2021/05/05')
    b3 = KeyboardButton('2021/06/01')
    b4 = KeyboardButton('2021/07/01')

    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

    kb_client.add(b1).row(b2).add(b3).row(b4)
    async with state.proxy() as data:
        data['valute'] = message.text
    await FSMAdmin.next()
    await message.answer("А теперь дату", reply_markup=kb_client)

#Получаем и сохраняем желаемую дату
@dp.message_handler(state=FSMAdmin.day)
async def day_selection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['day'] = message.text
    await message.answer("Секундочку...")
    async with state.proxy() as data:
        try:
            valute = data["valute"]
            day = data["day"]
            print(f"https://www.cbr-xml-daily.ru/archive/{day}/daily_json.js")
            req = requests.get(f"https://www.cbr-xml-daily.ru/archive/{day}/daily_json.js")
            response = req.json()
            eur = response["Valute"][f"{valute}"]["Value"]
            await message.reply(f"Дата: 2021/05/05\nКурс ЕВРО: {eur}")
        except:
            await message.reply("Проверьте валюту и дату")
    await state.finish()

#
# @dp.message_handler()
# async def get_valute(message: types.Message):
#     try:
#         req = requests.get(f"https://www.cbr-xml-daily.ru/archive/2021/05/05/daily_json.js")
#         response = req.json()
#         eur = response["Valute"][f"{message.text.upper()}"]["Value"]
#         await message.reply(f"Дата: 2021/05/05\nКурс ЕВРО: {eur}")
#     except:
#         await message.reply("Проверьте валюту и дату")

if __name__ == '__main__':
    executor.start_polling(dp)