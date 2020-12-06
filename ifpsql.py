#skbd_menu = {'PostgreSQL':postgresql_connect, 'MySQL':mysql_connect}
    menu = {'create':create, 'insert':insert,'read':read,'update':update,'delete':delete}#s, 'all tbs':tb_list}
    #print("Choose DB, please: ")
    #for key in skbd_menu.keys():
    #    print("-> "+key)
    #ans = input(">>")

"""
def table_exists(cur, conn, tb):
    cur.execute("SELECT tablename FROM PG_CATALOG.PG_TABLES where schemaname='public'")
    tblist = cur.fetchall()
    all_tbs=[]
    for row in tblist:              
        all_tbs.append(row['tablename'].lower())
    print(all_tbs)
    
    while tb.lower() not in all_tbs:
        print("Table doesn`t exist")
        tb = input_tb()
    return tb
"""

    
"""

def postgresql_connect():
    try:
        connection = psycopg2.connect(dbname='test_ps', 
                                        user='darina', 
                                        password='orirul89', 
                                        host='localhost')

        print("Connected successfully!")

        return [connection, connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)]
    except:
        print("Can`t connect! Please, check configuration!")
        """
