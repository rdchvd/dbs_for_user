from conditions import  cond
from mysql_types import  correct_type
from ifexist import table_exists
from read import read

def update(cur, conn, tb):
    tb = table_exists(cur, conn, tb)
    read(cur, conn, tb)
    ans = input("Ви хочете переназвати таблицю(1) або змінити колонки(2) чи значення(3)?")
    if ans != '1':
        cur.execute("SELECT * FROM "+tb)
        desc=cur.description
        col_names = [desc[i][0].lower() for i in range(len(desc))]
        
        if ans=='3':
            col = update_rows(cur,conn,tb, col_names)
            sql = "UPDATE "+tb+" SET "+col
        else:
            sql = update_columns(cur, conn, tb, col_names)
    else:
        sql = "ALTER TABLE {0} RENAME ".format(tb)
        tb = input('Введіть нову назву таблиці:')
        sql += tb
        
    
    try: 
        cur.execute(sql)
        conn.commit()
        print("Успішно змінено!")
        
    except:
        print('Не можу відредагувати!')
    ans = input("Ще одна зміна?так/ні: ")
    if ans=='так':
        update(cur, conn, tb)
    else:
        return




def update_rows(cur, conn, tb, col_names):

    
    updates=[]
    
    sql=""
    while True:
        col=""
        while col.lower() not in col_names:
            col = input('Виберіть колонку: ')
        val = input_format('Нове значення: ')

        sql += col + " = "
        
        if isinstance(val, str):
            sql+=("'{0}'".format(val))
        else:
            sql+=("{0}".format(val))

        condition = input("Якісь умови для редагування?так/ні: ")
        if condition == 'так':
            sql = cond(col_names, sql)
            
        break
        

    return sql




def update_columns(cur, conn, tb, col_names):
    sql = "ALTER TABLE {0}".format(tb)
    col =""
    ans = input('Що саме Ви бажаєте зробити з колонками?\n->додати нову(1)\n->видалити(2)\n->переназвати(3)\n->змінити тип(4)\n>>')
    if ans != '1':
        while col.lower() not in col_names:
            col = input('Введіть назву колонки: ')
            
        if ans == '2':
            sql += " DROP COLUMN {0}".format(col)
        else:
            cur.execute("DESCRIBE {0};".format(tb))
            rows = cur.fetchall()
            for row in rows:
                if row['Field'].lower() == col: 
                    typee = row['Type']
                    print(typee)
            sql += " CHANGE COLUMN {1}".format(tb, col)
            if ans == '4':
                    newtype = correct_type()
                    sql += " {0} {1}".format(col, newtype)

            else:
                newname = input('Нова назва:')
                sql += " {0} {1}".format(newname, typee)
    else:
        
        newname = input('Нова назва:')
        newtype = correct_type()
        sql += " ADD {0} {1}".format(newname, newtype)
        
        

    return sql

