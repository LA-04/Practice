import requests
import datetime
import xmltodict
import json
from auth_data import token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, InlineKeyboardButton
from aiogram_calendar import dialog_cal_callback, DialogCalendar

storage = MemoryStorage()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

b1 = KeyboardButton('EUR')
b2 = KeyboardButton('USD')
b3 = KeyboardButton('JPY')
b4 = KeyboardButton('CNY')
b5 = KeyboardButton('GBP')
b6 = KeyboardButton('SEK')
b7 = InlineKeyboardButton(text='Курс на сегодня', callback_data='archiv')
b8 = InlineKeyboardButton(text='Архивный курс', callback_data='archiv')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).insert(b4).add(b5).insert(b6)
kb_start.add(b7).insert(b8)

class FSMAdmin(StatesGroup):
    valute = State()
    day = State()

async def on_sturtup(_):
    print("Добрый день!")

#Начало диалога загрузки
@dp.message_handler(commands='start', state=None)
async def start(message: types.Message):

    await message.answer("Выберете действие:", reply_markup= kb_start)

@dp.message_handler(Text(equals=['Курс на сегодня'], ignore_case=True), state=None)
async def today(message: types.Message):
    try:
        d = datetime.datetime.now()
        day = datetime.date.strftime(d, "%d/%m/%Y")
        req = requests.get(f"https://cbr.ru/scripts/XML_daily.asp?date_req={day}")
        print(f"https://cbr.ru/scripts/XML_daily.asp?date_req={day}")
        xlm = req.content
        response = json.dumps(xmltodict.parse(xlm), indent=2, ensure_ascii=False)
        rec_json = json.loads(response)
        valutes = rec_json["ValCurs"]["Valute"]
        valutes_on_today = {info['Name']:info['Value'] for info in valutes}
        await message.answer(f"Дата: {day}\n")
        #{valutes_on_today}", reply_markup=kb_start
        for key, item in valutes_on_today.items():
            await message.answer(f"{key}: {item}", reply_markup=kb_start)
    except:
        await message.answer("Ошибка, попробуйте еще раз", reply_markup=kb_start)

    await message.answer("---Все валюты выгружены---", reply_markup= kb_start)

#выбора валюты
@dp.message_handler(Text(equals=['Архивный курс'], ignore_case=True), state=None)
async def archiv(message: types.Message):

    await FSMAdmin.valute.set()
    await message.answer("Выберете называние валюты:", reply_markup= kb_client)

#Получаем и сохраняем валюту
@dp.message_handler(state=FSMAdmin.valute)
async def valute_selection(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['valute'] = message.text

    await FSMAdmin.next()
    await message.answer("А теперь дату:", reply_markup=await DialogCalendar().start_calendar())

#Получаем и сохраняем желаемую дату
@dp.callback_query_handler(dialog_cal_callback.filter(), state=FSMAdmin.day)
async def day_selection(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'You selected {date.strftime("%d/%m/%Y")}'
        )

    async with state.proxy() as data:
        data['day'] = date.strftime("%d/%m/%Y")
    await callback_query.message.answer("Секундочку...")
    async with state.proxy() as data:
        try:
            day = data['day']
            valute = data['valute']
            req = requests.get(f"https://cbr.ru/scripts/XML_daily.asp?date_req={day}")
            print(f"https://cbr.ru/scripts/XML_daily.asp?date_req={day}")
            xlm = req.content
            response = json.dumps(xmltodict.parse(xlm), indent=2, ensure_ascii=False)
            rec_json = json.loads(response)
            valutes = rec_json["ValCurs"]["Valute"]
            for info in valutes:
                if info['CharCode'] == valute:
                    rate = info['Value']
                    name = info['Name']
            await callback_query.message.answer(f"Дата: {day}\nКурс {name}: {rate}", reply_markup=kb_start)
        except:
            await callback_query.message.answer("Ошибка, попробуйте еще раз", reply_markup=kb_start)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)