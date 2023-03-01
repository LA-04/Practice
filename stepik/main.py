import pandas as pd
import re

today = "01.03"
book = pd.read_excel('Birthdays_test.xlsx', sheet_name = 'Notifications')
# for i, row in book.iterrows():
#     if today in row['Дата рождения']:
#         print(i)
# book['Статус отправки'] = ["Отправлено" if today in row['Дата рождения'] else " " for i, row in book.iterrows()]
# re.fullmatch(pattern, string)
[print("Отправлено") if re.search(today,row['Дата рождения']) else print("ytn") for i, row in book.iterrows()]