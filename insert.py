from ifexist import table_exists

def input_format(st):
    a = input(st)

    try:
        a = int(a)

    except ValueError:
        if a.capitalize() in ['True', 'False']:
            a = bool(a.capitalize())
    return a


def insert(cur, conn, tb):

    tb = table_exists(cur, conn, tb)
    cur.execute('SELECT * FROM %s'%tb)
    desc=cur.description
    col_names = [desc[i][0] for i in range(len(desc))]
    while True:
        print('Таблиця має ', len(col_names), 'колонок: ', ", ".join(col_names))

            
            
        dic = insert_f(col_names)
        sql = "INSERT INTO %s ("%tb+", ".join(dic.keys())+") VALUES ("
        i=0
        for value in dic.values():
            i+=1
            if isinstance(value, str):
                sql+=("'{0}'".format(value))
            else:
                sql+=("{0}".format(value))
            if i < len(dic.values()):
                sql +=", "
        sql+=")"
            

        try:
            cur.execute(sql)
            conn.commit()
            print("Дані успішно записано!")
        except:
            print('Виникли проблеми з записом даних. Спробуйте ще раз!')
            insert_f(col_names, tb, cur, conn)

        cont = input("Ще один рядок? так/ні: ")    
        if cont=='ні':
            break






def insert_f(col_names):    
    dictionary={}
    i = 0
    while True:
        a = ""
        while a.upper() not in col_names:
            a = input('Виберіть колонку:')
        dictionary[a] = input_format('Введіть значення: ')
        i += 1  
        if i < len(col_names):
            cont = input("Внести дані до ще одної колонки? так/ні: ")
                 
            if cont=='ні':
                break
        else:
            break

    return dictionary

