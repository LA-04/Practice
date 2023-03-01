import pandas as pd
import datetime
import smtplib
import re
import win32com.client as win32

def det_data_str():
    today = datetime.datetime.now().strftime("%d.%m")
    return today


def read_excel(today):
    book = pd.read_excel('Birthdays_test.xlsx', sheet_name = 'Notifications')
    book['Статус отправки'] = [send_email(row["Имя Отчество"], row["Эл. Адрес сотрудника"]) if re.search(today,row['Дата рождения']) else " " for i, row in book.iterrows()]
    book.to_excel(r'Birthdays_test.xlsx', index= False, sheet_name = 'Notifications')


# def send_email(name, email):
#     sender = "email"  #Логин почты с которой будет сделана отправка
#     password = "password"  #Пароль от почты
#
#     smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#     smtpObj.starttls()
#     message = f"Поздравляю Вас, {name}, с замечательным днём, светлым и радостным праздником — днём Вашего рождения! \n" \
#               f"Пусть сегодня Вам улыбается удача, сбываются все загаданные желания, пусть своей теплотой и любовью Вас согревают родные и близкие люди.\n" \
#               f"Желаю здоровья, везения, бодрости и много поводов для того, чтобы почувствовать себя счастливым человеком!"
#
#     try:
#         smtpObj.login(sender, password)
#         smtpObj.sendmail(sender,email, f"Subject: С днем рождения! \n{message}".encode('utf-8'))
#
#         print(f"Письмо отправлено {name}")
#         return "Отправлено"
#
#     except Exception as ex:
#
#         print(f"Ошибка отправки почты {ex}")
#         return "Ошибка отправки почты"


def send_email(name, email):
    try:
        ol_app = win32.Dispatch('Outlook.Application')
        mailitem = ol_app.CreateItem(0)
        mailitem.Subject = 'С днем рождения!'
        mailitem.BodyFormat = 1
        mailitem.Body = f"Поздравляю Вас, {name}, с замечательным днём, светлым и радостным праздником — днём Вашего рождения! \n" \
                        f"Пусть сегодня Вам улыбается удача, сбываются все загаданные желания, пусть своей теплотой и любовью Вас согревают родные и близкие люди.\n" \
                        f"Желаю здоровья, везения, бодрости и много поводов для того, чтобы почувствовать себя счастливым человеком!"

        mailitem.To = f'{email}'

        mailitem.Display()
        mailitem.Save()
        mailitem.Send()

        print(f"Письмо отправлено {name}")
        return "Отправлено"

    except Exception as ex:

        print(f"Ошибка отправки почты {ex}")
        return "Ошибка отправки почты"


def main():
    read_excel(det_data_str())

if __name__ == "__main__":
    main()
