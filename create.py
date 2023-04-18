from mysql_types import correct_type

# ------ CREATE -----------


def create(cur, conn, tb):
    try:
        qq = create_f()
        sql = "create table if not exists {0}({1})".format(tb, qq)
        sql = sql.upper()

        cur.execute(sql)
        conn.commit()
        print("Створено таблицю {0}!".format(tb))
    except Exception:
        print("Не можу створити!")


def create_f():
    qq = ""
    pkflag = 0
    flag = 0

    while True:
        name = input("Назва колонки: ")
        type_ = correct_type()
        auto_incr = bool(int(input("Ви хочете, щоб вона заповнювалася автоматично? 1/0: ")))
        if auto_incr is True:
            auto_incr = "AUTO_INCREMENT"
            flag = 1
        else:
            auto_incr = ""

        if pkflag == 0:
            p_k = bool(int(input("Колонка має бути ключовою(ідентифікатором)? 1/0: ")))

            if p_k is True:
                pkflag = 1
                p_k = "primary key"
        else:
            p_k = ""

        if flag == 0:
            null_ = bool(int(input("Колонка може бути незаповненою? 1/0: ")))
            if null_ is True:
                null_ = "NULL"
            else:
                null_ = "NOT NULL"
                default = bool(int(input("Ви хочете поставити дефолтне(за замовчуванням) значення? 1/0: ")))
                if default is True:
                    val = input("Введіть дефолтне значення: ")
                    default = "DEFAULT " + val
                    null_ = ""
                else:
                    default = ""
        else:
            null_ = default = ""

        query = " ".join([name, type_, auto_incr, p_k, null_, default])
        qq += query

        cont = input("Ще одна колонка? так/ні: ")
        if cont == "так":
            qq += ","
        else:
            break
    return qq


#################################################
