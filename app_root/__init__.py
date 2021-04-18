from flask import Flask
from books.books import books_v1
app = Flask(__name__)

def create_app():
    #app.config.from_mapping(mysql_conection)
    app.register_blueprint(books_v1,url_prefix='/books/v1/')

    return app


