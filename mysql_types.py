mysql_types = [
    {"mtype": "char", "mdescription": "рядок з символами, до 255 символів"},
    {
        "mtype": "varchar",
        "mdescription": "те саме, що і char, але, якщо ви вирішите покласти сюди задовгий рядок, тип перетвориться на text",
    },
    {"mtype": "text", "mdescription": "дуже довгий рядок: до 65 тисяч символів"},
    {"mtype": "int", "mdescription": "ціле число великого діапазону значень"},
    {"mtype": "float", "mdescription": "число з плаваючою комою(дробне)"},
    {"mtype": "date", "mdescription": "дата формату YYYY-MM-DD"},
    {"mtype": "datetime", "mdescription": "дата + число (YYYY-MM-DD HH:MM:SS)"},
    {"mtype": "year", "mdescription": "рік(може бути YY(від 1970 до 2069) або YYYY)"},
    {"mtype": "time", "mdescription": ""},
    {"mtype": "blob", "mdescription": ""},
    {"mtype": "longblob", "mdescription": ""},
    {"mtype": "longtext", "mdescription": ""},
    {"mtype": "double", "mdescription": ""},
    {"mtype": "timestamp", "mdescription": ""},
]


def correct_type():
    type_ = input('Введіть тип колонки(щоб дізнатися основні типи, наберіть "\?t")\n>>')
    if type_ == "\?t":
        for msqltype in mysql_types:
            if msqltype["mdescription"] != "":
                print("->", msqltype["mtype"])
                print("", msqltype["mdescription"])

    while type_.lower() not in [tp["mtype"] for tp in mysql_types]:
        type_ = input("Введіть тип колонки: ")
    if type_.lower() in ["char", "varchar"]:
        kilk = int(input("Максимальна довжина рядку(кількість символів): "))
        type_ = type_ + "(%s)" % kilk
    return type_
