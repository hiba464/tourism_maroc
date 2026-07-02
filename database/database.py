import mysql.connector


def connect_db():

    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="tourism_maroc",
        port=3306
    )