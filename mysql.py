import pymysql.cursors

def connection_db():

    try:
        connection = pymysql.connect(host='localhost',
                                user='darina',
                                password='PASS',
                                db='test_ms',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        
        
        print("connected")
        return connection
    except:
        print("shit")


def create(cur, conn, tb):
    qq = create_f()
    sql = "create table {0}({1})".format(tb, qq)
    sql=sql.upper()
    print(sql)
    cur.execute(sql)
    conn.commit()
    print("Successfully created")        
    
    
def create_f():
    qq=""
    flag=0
    while True:
        name=input("Column name: ")
        type_=input("Type of column: ")
        if type_.lower() in ['char', 'varchar']:
            kilk=int(input('Max number of symbols: '))
            type_=type_+'(%s)'%kilk
        
        auto_incr=bool(int(input('Do you want it to be filled automatically? 1/0: ')))
        if auto_incr==True:
            auto_incr="AUTO_INCREMENT"
        else:
            auto_incr = ""

        if flag==0:
            p_k=bool(int(input('Is it primary key? 1/0: ')))
            if p_k==True:
                flag=1
                p_k="primary key"
        else:
            p_k=""

        null_=bool(int(input('Could that column be void? 1/0: ')))
        if null_==True:
            null_="NULL"
        else:
            null_="NOT NULL"
            default=bool(int(input('Do you wanna to set default value? 1/0: ')))
            if default==True:
                val = input('Input default value: ')
                default="DEFAULT "+val
                null_=""
            else:
                default = ""

        
        query= " ".join([name, type_, auto_incr, p_k, null_, default])
        qq += query

        cont = input("One else column? y/n: ")    
        if cont=='y':
            qq+=','
        else:
            break 
    return qq



def input_tb():
    tb=input('Input, please, name of tb: ')
    return tb

def new_tb(tb):
    answer=input('do you wanna continue working with table %s? y/n:'%tb)
    if answer == 'n':
        tb = input_tb()
    return tb

def insert_rows(tb, cur, conn):
    cur.execute('SELECT * FROM %s'%tb)
    desc=cur.description
    col_names = [desc[i][0] for i in range(len(desc))]
    while True:
        print('There are', len(col_names), 'columns: ', ", ".join(col_names))

        
        
        dic = insert(col_names)
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
            print("""REQUEST 
            '%s' 
            SUCCESSFULLY INSERTED
            """%sql)
        except:
            print('SMTH wrong with insertion. Try else!')
            insert_rows(col_names, tb, cur, conn)

        cont = input("One else row? y/n: ")    
        if cont=='n':
            break




    

def input_format(st):
    a = input(st)

    try:
        a = int(a)

    except ValueError:
        if a.capitalize() in ['True', 'False']:
            a = bool(a.capitalize())
        
    else:
        pass
    finally:
        pass
    return a
  
    




def insert(col_names):    
    dictionary={}
    i = 0
    while True:
        a = ""
        while a.upper() not in col_names:
            a = input('choose field:')
        dictionary[a] = input_format('input value: ')
        i += 1  
        if i < len(col_names):
            cont = input("One else column? y/n: ")
                 
            if cont=='n':
                break
        else:
            break
    print(dictionary)
    return dictionary


def cond(col_names, sql):
    
    conditions=[]
    col=""
    while True:
        while col.upper() not in col_names:
            col = input('choose a column: ')
        val = input_format('set a condition value: ')
        ans = input("do u wanna see rows with {0}={1}?y/n: ".format(col, val))
            
        col = col + " = "
        if isinstance(val, str):
            col+=("'{0}'".format(val))
        else:
            col+=("{0}".format(val))
               
        if ans=='n':
            col = "not " +col

        conditions.append(col)
       
        ans = input("one more condition?y/n: ")
        if ans=='n':
            break
        
    if len(conditions)>1:
        ans = input("do u wanna to set ALL rules or AS A MINIMUM ONE OF THEM?all/one: ")
        if ans.lower()=='all':
            cond =  " AND ".join(conditions)
        else: 
            cond =  " OR ".join(conditions)
            
    else:
        cond = conditions[0]
        
    sql = sql+' WHERE ' + cond.upper()

    return sql


def read(cur, conn, tb):
    
    sql = "SELECT * FROM "+tb
    cur.execute(sql)
    desc=cur.description
    col_names = [desc[i][0] for i in range(len(desc))]
    print('There are', len(col_names), 'columns: ', ", ".join(col_names))
    ifall = input("Do u wanna see all columns?y/n: ")
    if ifall == 'n':
        ifsome = input("Do u wanna see any of columns?y/n: ")
        if ifsome == 'n':
            return
        col = ""
        columns=[]
        while True:
            while col.upper() not in col_names:
                col = input('choose a column: ')
            columns.append(col)
            col=""
            
            ans = input("one else column?y/n: ")
            if ans == 'n':
                break

        sql = "SELECT "+(", ".join(columns)).upper()+" FROM "+tb      
        
        
    
    condition = input("Do u wanna to set some conditions?y/n")
    if condition == 'y':
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
        values = row.values()
        for value in values:
            print(f'{value:<10}', end="|")

        print()

def update(cur, conn, tb):
    read(cur, conn, tb)
    col = update_rows(cur,conn,tb)
    sql = "UPDATE "+tb+" SET "+col
    print(sql)


def update_rows(cur, conn, tb):
    
   
    cur.execute("SELECT * FROM "+tb)
    desc=cur.description
    col_names = [desc[i][0] for i in range(len(desc))]
    updates=[]
    
    sql=""
    while True:
        col=""
        while col.upper() not in col_names:
            col = input('choose a column: ')
        val = input_format('set a new value: ')

        sql += col + " = "
        print(sql)
        if isinstance(val, str):
            sql+=("'{0}'".format(val))
        else:
            sql+=("{0}".format(val))

        
        updates.append(col)
        
        
        condition = input("Do u wanna to set some conditions?y/n")
        if condition == 'y':
            sql = cond(col_names, sql)
            print(sql)
    
        #cur.execute(sql)

       
        ans = input("one more update?y/n: ")
        if ans=='y':
            sql+=", "
            print(sql)
            
        else:
            break

    return col

        
    """UPDATE Products
SET Manufacturer = 'Samsung Inc.'
WHERE Manufacturer = 'Samsung';"""

    
        






def main():
    conn=connection_db()
    cur = conn.cursor()
    tb = input_tb()
    #read(cur, conn, tb)
    update(cur, conn, tb)
    #rows= cur.fetchall()
    #print(rows)
    #row=rows[0]
    #col_names = [x for x in row]
    #print(col_names)
    
    #insert_rows(tb, cur, conn)

    #tb = new_tb(tb)
    




    #conn.commit()

main()

       
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

    #with connection.cursor() as cursor:
        # Read a single record
    #    sql = "SELECT `ID`, `password` FROM `users` WHERE `email`=%s"
    #    cursor.execute(sql, ('webmaster@python.org',))
    #    result = cursor.fetchone()
    #    print(result)
