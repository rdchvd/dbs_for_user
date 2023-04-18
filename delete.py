from conditions import cond
from ifexist import table_exists


def delete(cur, conn, tb):
    tb = table_exists(cur, conn, tb)
    try:
        ans = input("Ви бажаєте видалити таблицю(1) {0} або тільки деякі рядки(2)?".format(tb))

        if ans == "2":
            sql = "DELETE FROM {0}".format(tb)
            ans = input("Очистити таблицю {0}(1) чи видалити декілька рядків(2)?".format(tb))
            if ans == "2":
                sqlsel = "SELECT * FROM " + tb
                cur.execute(sqlsel)
                desc = cur.description
                col_names = [desc[i][0] for i in range(len(desc))]
                sql = cond(col_names, sql)
        else:
            sql = "DROP TABLE " + tb

        cur.execute(sql)
        conn.commit()
        print("Успішно видалено!")
    except Exception:
        print("Не можу видалити!")
