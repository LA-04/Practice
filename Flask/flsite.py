from flask import Flask, render_template, url_for, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase
from flask_sqlalchemy import SQLAlchemy

#Конфигурация
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'FDGSDHFJJSKAF789LKJLKJ4K4K4F'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

# menu = [{"name": "Установка", "url": "instal-flask"},
#         {"name": "Первое приложение", "url": "first-app"},
#         {"name": "Обратная связь", "url": "contact"}]

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """ Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    """Соединение с БД, если оно еще не установлено"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())

@app.route("/brands")
def brands():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('brands.html', menu=dbase.getMenu(), posts=dbase.getPostsAnonce())

@app.route("/brands/<path:url>")
def showBrands(url):
    db = get_db()
    dbase = FDataBase(db)
    brand_name, brand_img = dbase.getBrand(url)
    if not brand_name:
        abort(404)

    return render_template('post.html', menu=dbase.getMenu(), title = brand_name, post = brand_img)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title = "О сайте", menu=dbase.getMenu())

@app.route("/contact", methods=["POST", "GET"])
def contact():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено", category='success')
        else:
            flash("Ошибка отправки", category='error')

    return render_template('contact.html', title="Обратная связь", menu=dbase.getMenu())

@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с БД, если оно было установлено"""
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.errorhandler(404)
def pageNotFount(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title='Страница не найдена', menu=dbase.getMenu()    ), 404

if __name__ == "__main__":
    app.run(debug=True)
