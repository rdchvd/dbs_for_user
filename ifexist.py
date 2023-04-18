def input_tb():
    tb = input("Введіть назву таблиці: ")
    return tb


def table_exists(cur, conn, tb):

    all_tbs = table_check(cur, conn, tb)
    while tb not in all_tbs:
        print("Таблиця не існує!")
        tb = input_tb()
    return tb


def table_check(cur, conn, tb):
    cur.execute("SHOW TABLES")
    tblist = cur.fetchall()
    # print(tblist)
    all_tbs = []
    for tbdict in tblist:
        for value in tbdict.values():
            all_tbs.append(value)
    return all_tbs
