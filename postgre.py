import psycopg2


class POSTGRESQL:
    DB_NAME="test_ps"
    DB_USER="darina"
    DB_PASS="orirul89"
    DB_HOST="localhost"
    DB_PORT="5432"
    


    def __init__(self):
        try:
            self.conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, 
                                password=self.DB_PASS, host=self.DB_HOST)
<<<<<<< HEAD
            self.cur = self.conn.cursor()
=======
>>>>>>> 0a71fbd2914b51d299fc7da407a0f2570eecbeb7
            print('Successfully connected')
        except:
            print('problema conecto')

        

    def __del__(self):
        try:
            self.conn.close()
            print('Successfully disconnected. You can finish work ')
        except:
            print('U can`t dissconnect!')
        

<<<<<<< HEAD
    def create(self):
        try:
            self.cur.execute("""
            CREATE TABLE Stu1(
=======
    def create(cur, conn):
        try:
            cur.execute("""
            CREATE TABLE Student2(
>>>>>>> 0a71fbd2914b51d299fc7da407a0f2570eecbeb7
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                SURNAME TEXT NOT NULL
            )
            """)
<<<<<<< HEAD
            self.conn.commit()
=======
            conn.commit()
>>>>>>> 0a71fbd2914b51d299fc7da407a0f2570eecbeb7
            print("Successfully inserted")
        except:
            print('Prodblems with insertion')

<<<<<<< HEAD

    def inserting_data(self):
        try:
            self.cur.execute("INSERT INTO Student2(ID, NAME, SURNAME) VALUES(1, 'Darina', 'Rodicheva')")
            self.conn.commit()
=======
    def inserting_data(cur, conn):
        try:
            cur.execute("INSERT INTO Student2(ID, NAME, SURNAME) VALUES(1, 'Darina', 'Rodicheva')")
            conn.commit()
>>>>>>> 0a71fbd2914b51d299fc7da407a0f2570eecbeb7
            print("Successfully iserted data!")
        except:
            print("Problem with data!")

    def updating_data(cur, conn):
        try:
            cur.execute("UPDATE Student set NAME = 'Anton' WHERE ID=1")
            conn.commit()
            print("Successfully updated data!")
        except:
            print("Problem with updating!")

    def reading_data(cur, conn):
        try:
            cur.execute("SELECT NAME, SURNAME FROM Student")
            rows = cur.fetchall()

            for data in rows:
                print("NAME: "+data[0])
                print("SURNAME: "+data[1])
        except:
            print("Problem with reading data")

    def deleting_data(cur, conn):
        try:
            cur.execute("DELETE FROM Student WHERE ID=3")
            conn.commit()
            print("Successfully deleted data!")
        except:
            print("Problem with deleting!")

    



def main():
    db = POSTGRESQL()
    
<<<<<<< HEAD
    db.create()
=======
>>>>>>> 0a71fbd2914b51d299fc7da407a0f2570eecbeb7
    
 #   cur = conn.cursor()


    

<<<<<<< HEAD
#main()
=======
main()
>>>>>>> 0a71fbd2914b51d299fc7da407a0f2570eecbeb7
