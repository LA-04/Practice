from pprint import pprint

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
import pickle
import re
import os

options = webdriver.FirefoxOptions()
options.set_preference("general.userangent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


def save_stud_info(login, password):
        driver.get("https://e.muiv.ru/login/index.php")
        time.sleep(1)

        username_input = driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(login)
        time.sleep(1)

        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

       # pickle.dump(driver.get_cookies(), open(f"cookies/{login}_cookies", "wb"))

        return get_stud_info()
        # all_dis = all_dis.get_attribute('innerHTML').encode("UTF-8")
        # names_of_disciplines = all_dis.find_elements(By.CLASS_NAME, "dis_name")
        # disciplines_not_done = all_dis.find_elements(By.CLASS_NAME, "notdone")


def get_disciplines(all_dis):
    """Формируем словарь, где ключ - это название предмета, значение - список с предметами, у которых есть атрибут notdone"""
    order = {}

    for dis in all_dis:
        dis_name = dis.find_element(By.CLASS_NAME, "dis_name").text
        works_not_done = dis.find_elements(By.CLASS_NAME, "notdone")
        works_for_order = []

        for work_not_done in works_not_done:
            work = work_not_done.find_element(By.TAG_NAME, "a").text
            works_for_order.append(work)
        order[dis_name] = works_for_order

    # json_works = json.dumps(order, indent=4, ensure_ascii=False)
    return order


def cost_dis(disciplines):
    #Оценка всего семестра
    tests = 0
    print("Стоимость всего семестра")
    for dis, works in disciplines.items():
        test = 0
        for work in works:
            if "Тест " in work:
                test += 1
                tests += 1
            if "Рейтинговая работа " in work:
                reiting = work
        print(dis,":\n",f"всего тестов {test},\n {reiting}\n")
      #  print(dis,":",works)

    #Только тесты
    print("-"*10)
    print("Только тесты")
    tests = 0
    for dis, works in disciplines.items():
        test = 0
        for work in works:
            if "Тест " in work:
                test += 1
                tests += 1
        print(dis, ":", f"всего тестов {test}")
    print(f"Всего тестов: {tests}, стоимость {tests * 90}")
    print("От 75 баллов")
    # print(json_works)


def metodichki(all_dis):


# def use_cookies(login):
#     driver.get("https://e.muiv.ru/login/index.php")
#     time.sleep(1)
#
#     for cookie in pickle.load(open(f"cookies/{login}_cookies", "rb")):
#         driver.add_cookie(cookie)
#
#     time.sleep(1)
#     driver.refresh()
#     time.sleep(10)
#
#     get_stud_info()


def get_stud_info():
    all_dis = driver.find_elements(By.CLASS_NAME, "dis_block")
    return all_dis


if __name__ == '__main__':
    try:
        # login = input("Логин:")
        # password = input("Пароль:")
        login = "70178160"
        password = "BicikNuxa4555"

        disciplines = get_disciplines(save_stud_info(login, password))
        cost_dis(disciplines)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


#mod_block mod_quiz тест выполнен
#mod_block mod_quiz notdone не выполнен