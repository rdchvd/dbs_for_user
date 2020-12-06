
import psycopg2
import psycopg2.extras
from create import create
from insert import insert
from read import read
from delete import delete
from update import update
from mysqll_connection import *
from ifexist import table_check

def input_tb():
    tb=input('Введіть назву таблиці: ')
    return tb

def new_tb(tb):
    answer=input('Продовжити роботу з таблицею %s? так/ні: '%tb)
    if answer == 'ні':
        tb = input_tb()
    return tb



def input_format(st):
    a = input(st)

    try:
        a = int(a)

    except ValueError:
        if a.capitalize() in ['True', 'False']:
            a = bool(a.capitalize())
    return a


def tb_list(cur, conn, tb):
    cur.execute("SHOW TABLES")
    tblist = cur.fetchall()
    print(tblist)












def main():
    
    menu = {'вставити':insert,'вивести':read,'відредагувати':update,'видалити':delete}
    tb = None
    conn = mysql_connect()
    cur = conn.cursor()
    
    
    while True:
        
        tb = input_tb() if tb == None else new_tb(tb)
        all_tbs = table_check(cur, conn, tb)
        if tb not in all_tbs:
            ans = input("Такої таблиці не існує. Створити?так/ні: ")
            if ans == 'так':
                create(cur, conn, tb)
            else:
                tb = None
        else:

            print("Виберіть операцію: ")
            for key in menu.keys():
                print("-> "+key)
            ans = input(">>")
            menu[ans](cur, conn, tb)
            if ans == 'видалити':
                tb = None
        ans = input("Продовжити роботу?так/ні: ")
            
        if ans == 'ні':
            break

    conn.close()
    return

main()

 