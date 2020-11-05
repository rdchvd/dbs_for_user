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
            print('Successfully connected')
        except:
            print('problema conecto')

        

    def __del__(self):
        try:
            self.conn.close()
            print('Successfully disconnected. You can finish work ')
        except:
            print('U can`t dissconnect!')
        

    def create(cur, conn):
        try:
            cur.execute("""
            CREATE TABLE Student2(
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                SURNAME TEXT NOT NULL
            )
            """)
            conn.commit()
            print("Successfully inserted")
        except:
            print('Prodblems with insertion')

    def inserting_data(cur, conn):
        try:
            cur.execute("INSERT INTO Student2(ID, NAME, SURNAME) VALUES(1, 'Darina', 'Rodicheva')")
            conn.commit()
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
    
    
 #   cur = conn.cursor()


    

main()