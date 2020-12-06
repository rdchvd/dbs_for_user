from conditions import cond
from ifexist import table_exists


def read(cur, conn, tb):
    tb = table_exists(cur, conn, tb)
    sql = "SELECT * FROM "+tb
    cur.execute(sql)
    desc=cur.description
    col_names = [desc[i][0] for i in range(len(desc))]
    print('В таблиці', len(col_names), 'колонок: ', ", ".join(col_names))
    ifall = input("Ви хочете побачити всі колонки?так/ні: ")
    if ifall == 'ні':
        ifsome = input("Ви хочете побачити хоча б декілька з них?так/ні: ")
        if ifsome == 'ні':
            return
        col = ""
        columns=[]
        while True:
            while col.upper() not in col_names:
                col = input('Виберіть колонку: ')
            columns.append(col)
            col=""
                
            ans = input("Ще одну колонку?так/ні: ")
            if ans == 'ні':
                break

        sql = "SELECT "+(", ".join(columns)).upper()+" FROM "+tb      
            
            
        
    condition = input("Ви хочете поставити якісь умови для виведення?так/ні: ")
    if condition == 'так':
        sql = cond(col_names, sql)
        
    cur.execute(sql)
    rows = cur.fetchall()

    desc = cur.description
    print("|", end="")
    for i in range(len(desc)):

        print(f'{desc[i][0]:<10}', end="|")

    print()

    for row in rows:
        print("|", end="")
        for value in row.values():
            print(f'{str(value):<10}', end="|")

        print()

########################################################