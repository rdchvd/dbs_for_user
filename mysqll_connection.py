import pymysql.cursors

from config import CHOSEN_DB, DBHOST, DBPASS, DBUSER


def mysql_connect():
    try:
        connection = pymysql.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            db=CHOSEN_DB,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

        print("Під'єднано!")
        return connection
    except Exception:
        print("Не можу під'єднатись! Перевірте коректність даних!")
