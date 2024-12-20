import psycopg2 #to interact with postgreSQL
from config import config #module for database config

def connect():
    connection = None #sets to none
    try:
        params = config() #calls config function
        print('\033[32mConnection to PostgreSQL Database\033[0m (recipes)...')
        connection = psycopg2.connect(**params) #establishs connection with database using params from earlier

        crsr = connection.cursor() #creates cursor (bridge between code)
        print('\033[35mPostgreSQL Database version: \033[0m')
        crsr.execute('SELECT version()') #SQL query for version
        db_version = crsr.fetchone() 
        print(f'\033[35m{db_version}\033[0m') #displays version
        
        print("\n") #blank space

        crsr.execute("SELECT * FROM recipe_data") #TESTLINE
        rows = crsr.fetchall() #display all found

        for row in rows: #loops through rows
            print(row) #prints each row

        crsr.close() #closes cursor
        print("\n") #blank space
    except(Exception, psycopg2.DatabaseError) as error: #handles errors
        print(error)
    finally:
        if connection is not None: #ensures closurer of connection with database even if error
            connection.close()
            print('\033[33mDATABASE CONNECTION\033[0m \033[31mCLOSED\033[0m')
if __name__ == "__main__":
    connect()

