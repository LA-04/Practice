import sqlite3

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения БД")
        return []


    def getBrand(self, url):
        try:
            self.__cur.execute(f"SELECT brand_name, brand_img FROM brands WHERE url = '/{url}' LIMIT 1")
            res = self.__cur.fetchone()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД "+str(e))
        return (False, False)


    def getPostsAnonce(self):
        try:
            self.__cur.execute(f"SELECT * FROM brands")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД"+str(e))
        return []